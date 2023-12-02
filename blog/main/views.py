from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog, Review

# Create your views here.


def home(request: HttpRequest):

    review = Review.objects.all().order_by("-created_at")[0:5]
    return render(request, "main/home.html", {"review":  review, })


def add_blog(request: HttpRequest):
    if request.method == "POST":
        new_blog = Blog(
            name=request.POST["name"], paragraph=request.POST["paragraph"], release_date=request.POST["release_date"], category=request.POST["category"], image=request.FILES["image"])
        new_blog.save()

        return redirect("main:read_blog")

    return render(request, "main/add.html", {"categories": Blog.categories})


def read_blog(request: HttpRequest):

    if "category" in request.GET and request.GET["category"] == "Coffee":
        blog = Blog.objects.filter(category__icontains="Coffee")

    elif "category" in request.GET and request.GET["category"] == "Tea":
        blog = Blog.objects.filter(category__icontains="Tea")

    elif "category" in request.GET and request.GET["category"] == "Matcha":
        blog = Blog.objects.filter(category__icontains="Matcha")

    elif "category" in request.GET and request.GET["category"] == "Water":
        blog = Blog.objects.filter(category__icontains="Water")

    else:
        blog = Blog.objects.all()

    return render(request, "main/read.html", {"blog": blog})


def detail_blog(request: HttpRequest, blog_id):
    blog_detail = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        new_blog = Review(
            Blog=blog_detail, full_name=request.POST["full_name"], rating=request.POST["rating"], comment=request.POST["comment"])
        new_blog.save()

    review = Review.objects.filter(Blog=blog_detail)
    return render(request, "main/detail.html", {"blog": blog_detail, "review": review})


try:
    def update_blog(request: HttpRequest, blog_id):
        blog = Blog.objects.get(id=blog_id)

        if request.method == "POST":
            blog.name = request.POST["name"]
            blog.paragraph = request.POST["paragraph"]
            blog.release_date = request.POST["release_date"]
            blog.category = request.POST["category"]
            blog.image = request.FILES["image"]
            blog.save()

            return redirect("main:read_blog")
        return render(request, "main/update.html", {"blog": blog, "categories": Blog.categories})
except Exception as e:
    print(e)


def delete_blog(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("main:read_blog")


def search(request: HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        blog = Blog.objects.filter(name__icontains=keyword)
    else:
        blog = Blog.objects.all()

    return render(request, "main/search.html", {"blog": blog})
