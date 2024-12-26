from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Cart, Record
from products.models import Product
import stripe

# Set the Stripe secret key from settings
stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required(login_url='/accounts/login')
def addtocart(request, id):
    """Add a product to the user's cart."""
    product = get_object_or_404(Product, id=id)
    
    # Check if the product is already in the cart, if so, update the quantity
    cart_item, created = Cart.objects.get_or_create(product=product, loged_user=request.user)
    if not created:
        cart_item.quantity += 1  # Increase the quantity if the item already exists in the cart
        cart_item.save()
    
    return redirect('home_page')

@login_required(login_url='/accounts/login')
def update_cart_quantity(request, id):
    """Update the quantity of a product in the user's cart."""
    cart_item = get_object_or_404(Cart, id=id, loged_user=request.user)
    
    if request.method == 'POST':
        # Assuming the quantity is being sent as a POST parameter
        quantity = int(request.POST.get('quantity'))
        cart_item.quantity = quantity  # Update the quantity field
        cart_item.save()

    return redirect('cart')  # Redirect back to the cart page

@login_required(login_url='/accounts/login')
def cart(request):
    """Display the contents of the user's cart."""
    cart_items = Cart.objects.filter(loged_user=request.user)
    total_price = sum(item.product.price for item in cart_items)
    context = {
        'cart': cart_items,
        'total_price': total_price,
        "quantity_range": range(1, 11),
    }
    return render(request, 'cart.html', context)


@login_required(login_url='/accounts/login')
def removefromcart(request, id):
    """Remove a product from the user's cart."""
    cart_item = get_object_or_404(Cart, id=id, loged_user=request.user)
    cart_item.delete()
    return redirect('/cart')


@login_required(login_url='/accounts/login')
def checkout(request):
    """Display the checkout page."""
    return render(request, 'checkout.html', {'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY})


@login_required(login_url='/accounts/login')
@csrf_exempt
def checkoutpro(request):
    """Handle the checkout process and create a Stripe session."""
    YOUR_DOMAIN = 'https://seafoodsell.pythonanywhere.com/'
    try:
        cart_items = Cart.objects.filter(loged_user=request.user)
        if not cart_items.exists():
            return JsonResponse({'error': 'Cart is empty.'}, status=400)

        total_price = sum(item.product.price for item in cart_items)
        if total_price <= 0:
            return JsonResponse({'error': 'Invalid cart total.'}, status=400)

        # Create Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(total_price * 100),
                        'product_data': {'name': 'Seafood Sell'},
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return JsonResponse({'id': checkout_session.id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def success(request):
    """Handle successful payments."""
    session_id = request.GET.get('session_id')
    if not session_id:
        return redirect('/cart')  # Redirect if session ID is missing

    try:
        # Retrieve the Stripe session and line items
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        line_items = stripe.checkout.Session.list_line_items(session_id)

        # Record the payment in the database
        Record.objects.create(
            customer_email=checkout_session.customer_details.email,
            amount_total=checkout_session.amount_total / 100,
            payment_intent=checkout_session.payment_intent,
            payment_id=checkout_session.id,
            status=checkout_session.payment_status,
        )

        # Clear the user's cart
        Cart.objects.filter(loged_user=request.user).delete()
        return render(request, 'success.html')

    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)


def cancel(request):
    """Handle cancelled payments."""
    return render(request, 'cancel.html')
