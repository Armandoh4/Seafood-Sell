from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/") 
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect("login") 
    return render(request,'accounts/login.html')

def signup(request):
    return render(request,'accounts/sign_up.html')


def sign_in(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(email=email).exists() or User.objects.filter(username=name).exists():
                messages.error(request, 'Username or Email address already exists!')
                return render(request,'accounts/sign_up.html')
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                messages.success(request, 'Your account is successfully created')
                user.save()
                return redirect("login")
    
    

def logout_view(request):
    logout(request)
    return redirect('login')
