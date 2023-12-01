from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
# Create your views here.

def signup_view(request:HttpRequest):
    if request.method=='POST':
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['last_name']  )
        user.save()
        return redirect('accounts:signin')
    return render(request,'accounts/signup.html')

def signin_view(request:HttpRequest):
    
    msg =None

    if request.method == 'POST':
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        
        if user:
            login(request,user)
            return redirect('main:home')
        else: msg = "please provide correct user name and password"

    return render(request,'accounts/signin.html',{'msg':msg})

def log_out_user(request:HttpRequest):
    
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:signin')
