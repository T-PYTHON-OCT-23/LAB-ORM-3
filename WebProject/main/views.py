from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from blogs.models import Blog, Review

# Create your views here.

def home_view(request: HttpRequest):

    
    #accessing the logged in user info
    if request.user.is_authenticated:
        print(request.user.first_name)
    
    reviews = Review.objects.all().order_by("-published_at")[0:5]
    review_count = reviews.count()

    return render(request,"main/index.html",{"reviews" : reviews, "review_count": review_count})


