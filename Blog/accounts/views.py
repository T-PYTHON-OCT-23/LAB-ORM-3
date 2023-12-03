from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_user(request :HttpRequest):
    msg= None
    if request.method == "POST":
        try:
            user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
            user.save()
            return redirect("accounts:login_user")
        except Exception as e:
          msg= f"The username exists, please enter another username {e}"
    
    return render(request, "accounts/register.html", {"msg" : msg})



def login_user(request: HttpRequest):
    msg = None
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            login(request, user)
            return redirect("main:home")
        else:
            msg = "Please provide correct username and password"



    return render(request, "accounts/login.html", {"msg" : msg})



def logout_user(request: HttpRequest):
    if request.user.is_authenticated:
        logout(request)    

    return redirect("main:home")

