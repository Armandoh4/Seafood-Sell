from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return render(request,'accounts/login.html')

def signup(request):
    return render(request,'accounts/sign_up.html')