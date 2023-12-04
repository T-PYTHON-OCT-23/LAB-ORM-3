from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog , Review
from django.utils import timezone
# Create your views here.


def add_blog_view(request: HttpRequest):
     
    if not request.user.is_staff:
        return render(request, 'main/not_authorized.html' , status=401)
    
    message = None
    if request.method == "POST":
      try:
         new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=timezone.now(),category=request.POST["category"],poster=request.FILES["poster"])
        
       
         if "poster" in request.FILES:
            new_blog .poster = request.FILES["poster"]

         new_blog.save()

         return redirect("post:display_blog_view")
      except Exception as e:
        message = f"An error occured, please fill in all fields and try again . {e}"


    return render(request, "post/add_post.html" , {"categories" : Blog.categories ,  "message" : message})


def display_blog_view(request: HttpRequest):
     
    if "category" in request.GET and request.GET["category"] == "Educationl":
         posts = Blog.objects.filter( category__contains="Educationl")[0:10]
         
    elif "category" in request.GET and request.GET["category"] == "Art":
         posts = Blog.objects.filter( category__contains="Art")[0:10]
   
    elif "category" in request.GET and request.GET["category"] == "Cultual":
         posts = Blog.objects.filter( category__contains="Cultual")[0:10]

    
    elif "category" in request.GET and request.GET["category"] == "Podcast":
         posts = Blog.objects.filter( category__contains="Podcast")[0:10]

    
    elif "category" in request.GET and request.GET["category"] == "Corporate":
         posts = Blog.objects.filter( category__contains="Corporate")[0:10]
                    
    else:
     
         posts = Blog.objects.all().order_by("published_at")

    
    posts_count = posts.count()  

    return render(request, "post/display_blog.html", {"posts": posts , "posts_count" : posts_count})


def post_detail_view(request:HttpRequest, post_id):
   
    try:
     post=Blog.objects.get(id=post_id )

     if request.method == "POST":
         new_review = Review(post=post, full_name=request.POST["full_name"], rating=request.POST["rating"], comment=request.POST["comment"])
         new_review.save()
    except Exception as e:
       return render(request, "post/not_exist.html")
    post_reviews = Review.objects.filter(post=post)

    return render(request, "post/post_detail.html", {"post" : post , "reviews" :post_reviews})


def not_exist_view(request:HttpRequest):

   return render(request, "post/not_exist.html")



def update_post_view(request: HttpRequest, post_id):

    if not request.user.is_staff:
        return render(request, "post/not_authorized.html", status=401)

    post = Blog.objects.get(id=post_id)

    if request.method == "POST":
        post.title = request.POST["title"]
        post.content= request.POST["content"]
        post.is_published = request.POST["is_published"]
        post.published_at = request.POST["published_at"]
        post.category = request.POST["category"]
        if "poster" in request.FILES:
            post.poster=request.FILES["poster"]
        post.save()

        return redirect('post:post_detail_view', post_id=post.id)

    return render(request, "post/update.html", {"post" : post , "categories"  : Blog.categories})

 
def delete_post_view(request: HttpRequest, post_id):

    if not request.user.is_superuser:
        return render(request, "post/not_authorized.html", status=401)

    post = Blog.objects.get(id=post_id)
    post.delete()

    return redirect("post:display_blog_view")


def search_post_view(request:HttpRequest ):
 # search_word=request.get["search"]
  
    if "search" in request.GET:
        key = request.GET["search"]
        posts = Blog.objects.filter(title__icontains=key)
    else:
        posts = Blog.objects.all()


    return render(request, "post/search.html", {"posts" :posts})



def display_blog_view_cat(request: HttpRequest, cat):

    posts=Blog.objects.filter(category=cat).order_by("-published_at")[0:5]
    posts_count = posts.count()

    return render(request, "post/display_blog.html", {"posts" : posts, "posts_count" : posts_count})


def add_review(request: HttpRequest,post_id):

    if request.method == "POST":

        if not request.user.is_authenticated:
            return render(request, "post/not_authorized.html", status=401)

        post_obj = Blog.objects.get(id=post_id)
        new_review = Review(post=post_obj,  full_name=request.POST["full_name"], rating=request.POST["rating"], comment=request.POST["comment"])  
        new_review.save()
        return redirect("post:post_detail_view", post_id=post_obj.id) 