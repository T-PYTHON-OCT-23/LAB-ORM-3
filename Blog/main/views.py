from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from blogs.models import Blog, Review

def home_view(request:HttpRequest):
    Reviews_last = Review.objects.all().order_by("-created_at")[0:5]
    blogs_last = Blog.objects.all().order_by("-published_at")[0:5]


    return render(request,"main/home.html",{"Reviews":Reviews_last ,"blogs":blogs_last})