from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def homePage(request : HttpRequest):

    return render(request ,"main/home.html")

