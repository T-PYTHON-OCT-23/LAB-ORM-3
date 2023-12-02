from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def sign_up_view (request:HttpRequest):

   if request.method == "POST":
        #create a new user
        user = User.objects.create_user(username=request.POST["username"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
        user.save()
        return redirect("account:sign_in_view")

   return render(request, "account/sign_up.html")


def sign_in_view(request:HttpRequest):
    msg=None
# authenticate user
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password= request.POST["password"])

        if user:
                login(request, user) #sign in user
                return redirect("main:home_view")
        else:
                msg = "Please provide correct username and password"

    return render(request, "account/sign_in.html", {"msg" : msg})



def sign_out_view(request: HttpRequest):
   
    if request.user.is_authenticated:
        logout(request)
    
    return redirect("account:sign_in_view")
     