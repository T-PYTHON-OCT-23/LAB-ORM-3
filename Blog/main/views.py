from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blogs.models import Blog ,Review
# Create your views here.

def home(request : HttpRequest):
    
    reviews = Review.objects.all().order_by("-date_add")[0:5]
    return render(request,'main/home.html', {"reviews" : reviews})

