from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='/accounts/login')
def index(request):
    print(request.user)
    categorie = Categorie.objects.all()
    product = Product.objects.all()
    cata = request.GET.get('categorie')

    if cata:
        product = product.filter(Categorie__categorie = cata)
    context = {
        "categorie" : categorie,
        'product':product,
    }
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'aboutus.html')
