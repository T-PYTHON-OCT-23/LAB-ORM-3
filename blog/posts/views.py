from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post , Review
from django.utils import timezone
import sqlite3

def add_blog_view(request: HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], is_publishd= True if "is_publishd" in request.POST else False, publishd_at=timezone.now()  ,  category=request.POST["category"])
        if 'poster' in request.FILES:
            new_post.poster = request.FILES["poster"]
        new_post.save()

        return redirect("posts:post_home_view")

    return render(request, "posts/add.html" , {"categories" : Post.categories})

def post_home_view(request: HttpRequest):

    reviews = Review.objects.all().order_by("-created_at")[0:5]

    posts = Post.objects.all()
    if "search" in request.GET:
        keyword = request.GET["search"]
        posts = Post.objects.filter(title__icontains=keyword)
    else:
        posts = Post.objects.all()

    return render(request, "posts/blog_home.html", {"posts" :posts , "reviews" :reviews})


try:
    def post_detail_view(request:HttpRequest, posts_id):
    
        posts = Post.objects.get(id=posts_id)
        if request.method == "POST":
            #create the review entry
            nReview = Review(post=posts, full_name=request.POST["full_name"], rating=request.POST["rating"], comment=request.POST["comment"])
            nReview.save()

        reviews = Review.objects.filter(post=posts)
        return render(request, "posts/blog_detail.html", {"posts" : posts ,"reviews" : reviews})

except sqlite3.Error as er:
            print('SQLite error:404')




def update_post_view(request: HttpRequest, posts_id):

    posts = Post.objects.get(id=posts_id)

    if request.method == "POST":
        posts.title = request.POST["title"]
        posts.content = request.POST["content"]
        # posts.is_publishd = request.POST["is_publishd"]
        posts.publishd_at = request.POST["publishd_at"]
        posts.category = request.POST["category"]
        if 'poster' in request.FILES:
            posts.poster= request.FILES["poster"]
        posts.save()

        return redirect('posts:post_detail_view', posts_id=posts.id)

    return render(request, "posts/update.html", {"posts" : posts , "categories"  : Post.categories})


def delete_post_view(request: HttpRequest, posts_id):

    posts = Post.objects.get(id=posts_id)
    posts.delete()

    return redirect("posts:post_home_view")


def display_Blog_views(request : HttpRequest , item):
    if item == 'Fashion':
        posts = Post.objects.filter(category ="Fashion")

    elif item == 'Personal_blogs':
        posts = Post.objects.filter(category ="Personal blogs") 
    
    elif item == 'Lifestyle':
        posts = Post.objects.filter(category ="Lifestyle")
    
    elif item == 'News_blogs':
        posts = Post.objects.filter(category ="News blogs")

    elif item == 'technology':
        posts = Post.objects.filter(category ="technology")

    else:
        posts = Post.objects.all()

    return render(request , 'posts/blog_home.html' , {"posts" : posts})