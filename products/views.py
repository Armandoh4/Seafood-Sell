from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.conf import settings
import stripe
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required(login_url='/accounts/login')

def index(request):
    print(request.user)
    categorie = Categorie.objects.all()
    product = Product.objects.all()
    len_of_cart = Cart.objects.filter(loged_user=request.user).count()
    cata = request.GET.get('categorie')

    if cata:
        product = product.filter(Categorie__categorie = cata)
    context = {
        "categorie" : categorie,
        'product':product,
        'len_of_cart':len_of_cart,
    }
    return render(request,'index.html',context)
@login_required(login_url='/accounts/login')
def addtocart(request,id):
    product = Product.objects.get(id = id)
    Cart.objects.create(product=product,loged_user=request.user)
    len_of_cart = Cart.objects.filter(loged_user=request.user).count()
    return redirect('home_page')
# @login_required(login_url='/accounts/login')
def aboutus(request):
    len_of_cart = 0
    if request.user.is_authenticated:
        len_of_cart = Cart.objects.filter(loged_user=request.user).count()
    return render(request,'aboutus.html',{'len_of_cart':len_of_cart})
@login_required(login_url='/accounts/login')
def cart(request):
    STRIPE_PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY
    if request.user:
        cart = Cart.objects.filter(loged_user = request.user)
        len_of_cart = Cart.objects.filter(loged_user=request.user).count()
        total_price = 0
        for i in cart :
            total_price += i.product.price
        context = {
            'cart':cart,
            'total_price':total_price,
            'len_of_cart':len_of_cart,
            'stripe_public_key':STRIPE_PUBLISHABLE_KEY
        }
        return render(request,'cart.html',context)
@login_required(login_url='/accounts/login') 
def removefromcart(request,id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('/cart')



@login_required(login_url='/accounts/login')
def checkout(request):
    STRIPE_PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY
    
    return render(request,'checkout.html',{'stripe_public_key':STRIPE_PUBLISHABLE_KEY})


@login_required(login_url='/accounts/login')


@csrf_exempt
def checkoutpro(request):
    YOUR_DOMAIN = 'http://127.0.0.1:8000'

    try:
        cart = Cart.objects.filter(loged_user=request.user)
        total_price = sum(item.product.price for item in cart)
        
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
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        print('Checkout Session URL:', checkout_session.url)
        return JsonResponse({'id': checkout_session.id})

    except Exception as e:
        print('Error:', e)
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', None)
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.WEBHOOK_SECRET_KEY
        )
    except ValueError as e:
        # Invalid payload
        print('Invalid payload:', e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('Invalid signature:', e)
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_checkout_session(session)

    return JsonResponse({'status': 'success'})

def handle_checkout_session(session):
    # Retrieve the necessary data from the session object
    customer_email = session.get('customer_details', {}).get('email')
    amount_total = session.get('amount_total')
    payment_intent = session.get('payment_intent')
    Record.objects.create(
        customer_email=customer_email,
        amount_total=amount_total,
        payment_intent=payment_intent
    )
    print(session)
def success(request):
         
        cart = Cart.objects.filter(loged_user = request.user)
        for item in cart:
            item.delete()
            print('delete')
        return render(request,'success.html')
def cancel(request):
    return render(request,'cancel.html')
def detail(request,id):
    product = Product.objects.get(pk = id)
    len_of_cart = Cart.objects.filter(loged_user=request.user).count()
    return render(request,'details.html',{'product': product, 'len_of_cart': len_of_cart})
