from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
def home_page_views(request:HttpRequest):

    return render(request, 'home/base.html')