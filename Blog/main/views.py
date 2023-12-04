from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from post.models import Blog, Review
# Create your views here.

def home_view(request: HttpRequest):

  #  if request.user.is_authenticated:
 #       print(request.user.first_name)

    blogs = Blog.objects.all().order_by("-published_at")[0:5]
    reviews =Review.objects.all().order_by("-created_at")[0:5]

    return render(request, "main/index.html" , {"blogs" : blogs,"reviews" : reviews})
