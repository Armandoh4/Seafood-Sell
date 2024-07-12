from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
from django.contrib.auth.decorators import login_required
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

def addtocart(request,id):
    product = Product.objects.get(id = id)
    Cart.objects.create(product=product,loged_user=request.user)
    len_of_cart = Cart.objects.filter(loged_user=request.user).count()
    return redirect('home_page')
def aboutus(request):
    len_of_cart = 0
    if request.user.is_authenticated:
        len_of_cart = Cart.objects.filter(loged_user=request.user).count()
    return render(request,'aboutus.html',{'len_of_cart':len_of_cart})
def cart(request):
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
        }
        return render(request,'cart.html',context)
    
def removefromcart(request,id):
    cart = Cart.objects.get(id=id)
    cart.delete()
    return redirect('/cart')
