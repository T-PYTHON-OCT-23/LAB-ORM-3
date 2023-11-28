from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse


def home_views(request:HttpRequest):
    return render(request,"main/home.html")