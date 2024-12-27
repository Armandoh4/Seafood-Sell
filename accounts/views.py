from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

# View to handle user login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name', '').strip()
        password = request.POST.get('password', '').strip()

        # Validate input fields
        if not username or not password:
            messages.error(request, 'Username and Password are required.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect("/")
        else:
            messages.error(request, 'Incorrect Username or Password.')
            return redirect('login')

    return render(request, 'accounts/login.html')

# View to display the signup page and handle user registration
def signup(request):
    return render(request, 'accounts/sign_up.html')

# View to handle user signup
def sign_in(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        # Validate input fields
        if not name or not email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'accounts/sign_up.html')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters long.')
            return render(request, 'accounts/sign_up.html')

        if User.objects.filter(username=name).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'accounts/sign_up.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email address already exists.')
            return render(request, 'accounts/sign_up.html')

        try:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            messages.success(request, 'Your account has been successfully created. Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'accounts/sign_up.html')

    return render(request, 'accounts/sign_up.html')

# View to handle user logout
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
    return redirect('login')
