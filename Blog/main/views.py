from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blogs.models import Blog ,Review
# Create your views here.

def home(request : HttpRequest):
    if request.user.is_authenticated:
        print(request.user.first_name)

    reviews = Review.objects.all().order_by("-date_add")[0:5]
    blogs = Blog.objects.all().order_by("-published_at")[0:3]
    return render(request,'main/home.html', {"reviews" : reviews , "blogs":blogs})


def error(request : HttpRequest):
    return render(request,'main/not_authorized.html')

