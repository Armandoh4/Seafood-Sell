from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .models import Categorie, Product
from cart.models import Cart
import stripe

# Set the Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

# Index view to display categories and products
def index(request):
    categories = Categorie.objects.all()
    products = Product.objects.prefetch_related('productimg').all()  # Optimized query
     # Construct the full URL
    full_url = f"{request.scheme}://{request.get_host()}/"
    # Get the current host (domain)

    len_of_cart = Cart.objects.filter(loged_user=request.user).count() if request.user.is_authenticated else 0

    selected_category = request.GET.get('categorie')
    if selected_category:
        products = products.filter(Categorie__categorie=selected_category)

    context = {
        "categories": categories,
        'products': products,
        'len_of_cart': len_of_cart,
        'full_url': full_url,
    }
    return render(request, 'index.html', context)

# View to add a product to the cart
@login_required(login_url='/accounts/login')
def addtocart(request, id):
    product = get_object_or_404(Product, id=id)
    
    # Try to get the cart item for the current product and logged-in user
    cart_item = Cart.objects.filter(product=product, loged_user=request.user).first()
    
    if cart_item:
        # If the product already exists in the cart, update the quantity
        cart_item.quantity += 1
        cart_item.save()
    else:
        # If the product doesn't exist, create a new cart item with quantity 1
        Cart.objects.create(product=product, loged_user=request.user, quantity=1)
    
    return redirect('cart')

# View to display the about us page
def aboutus(request):
    len_of_cart = Cart.objects.filter(loged_user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'aboutus.html', {'len_of_cart': len_of_cart})

# View to display the cart and its contents
@login_required(login_url='/accounts/login')
def cart(request):
    STRIPE_PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY
    cart_items = Cart.objects.filter(loged_user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)  # Calculate price with quantity
    len_of_cart = cart_items.count()

    context = {
        'cart': cart_items,
        'total_price': total_price,
        'len_of_cart': len_of_cart,
        'stripe_public_key': STRIPE_PUBLISHABLE_KEY,
        "quantity_range": range(1, 11),
    }
    return render(request, 'cart.html', context)

# View to remove a product from the cart
@login_required(login_url='/accounts/login')
def removefromcart(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    cart_item.delete()
    return redirect('/cart')

# View to display the checkout page
@login_required(login_url='/accounts/login')
def checkout(request):
    return render(request, 'checkout.html', {'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY})

# View to handle the checkout process
@login_required(login_url='/accounts/login')
@csrf_exempt
def checkoutpro(request):
    YOUR_DOMAIN = f"{request.scheme}://{request.get_host()}/"
    try:
        cart_items = Cart.objects.filter(loged_user=request.user)
        if not cart_items:
            return JsonResponse({'error': 'Cart is empty'}, status=400)

        total_price = sum(item.product.price * item.quantity for item in cart_items)  # Correct price calculation

        # Create Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(total_price * 100),  # Correct price handling
                        'product_data': {'name': "Seafood Sell"},
                    },
                    'quantity': 1,  # The quantity will be handled per line item in Stripe
                }
            ],
            mode='payment',
            success_url=f"{YOUR_DOMAIN}/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{YOUR_DOMAIN}/cancel",
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

# View to handle successful payments
@login_required(login_url='/accounts/login')
def success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        Cart.objects.filter(loged_user=request.user).delete()
        return render(request, 'success.html')
    return redirect('cart')

# View to handle cancelled payments
def cancel(request):
    return render(request, 'cancel.html')

# View to display the details of a product
def detail(request, id):
    product = get_object_or_404(Product.objects.prefetch_related('productimg'), pk=id)
    len_of_cart = Cart.objects.filter(loged_user=request.user).count() if request.user.is_authenticated else 0
    return render(request, 'details.html', {'product': product, 'len_of_cart': len_of_cart})

# View to update the quantity of a product in the cart
@login_required(login_url='/accounts/login')
def update_cart_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id, loged_user=request.user)
    
    # Get the new quantity from the form
    new_quantity = request.POST.get('quantity')
    
    # Update the quantity if it's a valid number
    if new_quantity and new_quantity.isdigit():
        cart_item.quantity = int(new_quantity)
        cart_item.save()
    
    return redirect('cart')
