from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from posts.models import * 

# Create your views here.
def home_view(request: HttpRequest):
    reviews = Review.objects.all().order_by("-created_at")[0:5]
    

    return render(request, "main/home.html", {"reviews" :reviews})
