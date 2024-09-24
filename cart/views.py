from django.shortcuts import render, HttpResponse, redirect
from .models import *
from products.models import *
from django.conf import settings
import stripe
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse 
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Set the Stripe secret key from settings
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required(login_url='/accounts/login')
def addtocart(request, id):
    product = Product.objects.get(id=id)
    Cart.objects.create(product=product, loged_user=request.user)
    len_of_cart = Cart.objects.filter(loged_user=request.user).count()
    return redirect('home_page')
 
# View to display the cart and its contents
@login_required(login_url='/accounts/login')
def cart(request):
    STRIPE_PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY
    if request.user:
        cart = Cart.objects.filter(loged_user=request.user)
        len_of_cart = Cart.objects.filter(loged_user=request.user).count()
        total_price = 0
        for i in cart:
            total_price += i.product.price
        context = {
            'cart': cart,
            'total_price': total_price,
            'len_of_cart': len_of_cart,
            'stripe_public_key': STRIPE_PUBLISHABLE_KEY
        }
        return render(request, 'cart.html', context)

# def item_quantity(request):
#     for i in item_quantity:
        
def get_qty_cart(request):
    if request.method == 'POST':
        console.log('Quantity test 1')
        # Request the integer value of the id element of "qty-cart"
        qty_cart_value = int(request.POST.get('qty-cart', 1))
        
        # Create a console for loop that prints the integer value of "qty-cart" element
        for i in range(qty_cart_value):
            print(f"qty-cart value is: {qty_cart_value}")
         
        return HttpResponse(f"Received qty-cart value: {qty_cart_value}")
    else:
        return render(request, 'your_templa te.html')


# View to remove a product from the cart
@login_required(login_url='/accounts/login')
def removefromcart(request, id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('/cart')

# View to display the checkout page
@login_required(login_url='/accounts/login')
def checkout(request):
    STRIPE_PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'checkout.html', {'stripe_public_key': STRIPE_PUBLISHABLE_KEY})

# View to handle the checkout process
@login_required(login_url='/accounts/login')
@csrf_exempt
def checkoutpro(request):
    YOUR_DOMAIN = 'https://seafoodsell.pythonanywhere.com/'
    try:
        cart = Cart.objects.filter(loged_user=request.user)
        total_price = sum(item.product.price for item in cart)

        # Create a Stripe checkout session
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(total_price * 100),
                        'product_data': {
                            'name': "seafood-sell",
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return JsonResponse({'id': checkout_session.id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

# View to handle successful payments
def success(request):
    session_id = request.GET.get('session_id')
    if session_id:
        # Retrieve the session
        checkout_session = stripe.checkout.Session.retrieve(session_id)
        line_items = stripe.checkout.Session.list_line_items(session_id)
        
        # Record the payment details in the database
        Record.objects.create(
            customer_email=checkout_session.customer_details.email,
            amount_total=checkout_session.amount_total/100,
            payment_intent=checkout_session.payment_intent,
            payment_id=checkout_session.id,
            status=checkout_session.payment_status
        )
        
        # Clear the cart for the logged-in user
        cart = Cart.objects.filter(loged_user=request.user)
        for item in cart:
            item.delete()
        return render(request, 'success.html')
    
    # Clear the cart even if session_id is not found (fallback)
    cart = Cart.objects.filter(loged_user=request.user)
    for item in cart:
        item.delete()
    return render(request, 'success.html')

# View to handle cancelled payments
def cancel(request):
    return render(request, 'cancel.html')

# View to display the details of a product
