from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog, Review 

# Create your views here.

def add_blog_view(request: HttpRequest):
    #Creating a new entry into the database for a movie
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"],  category=request.POST["category"]  , 
            content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"] 
            , rating = request.POST["rating"], poster=request.FILES["poster"])
        new_blog.save()

        return redirect("blog:read_blog_view")

    return render(request,"blog/addBlog.html", {"categories" : Blog.categories})


def read_blog_view(request: HttpRequest):
    
    if "sort" in request.GET and request.GET["sort"] == "oldest":
        blog = Blog.objects.all().order_by("published_at")[0:]
    else:
        blog = Blog.objects.all().order_by("-rating")[0:]

    blog_count = blog.count()

    return render(request, "blog/blog_home.html", {"blog" : blog , "blog_count" : blog_count})


def blog_detail_view(request:HttpRequest, blog_id):

    blog_detail = Blog.objects.get(id=blog_id)

    if request.method=="POST":
        review = Review(blog=blog_detail ,name=request.POST["name"] ,review=request.POST["review"] , rating=request.POST["rating"] )
        review.save()

    reviews = Review.objects.filter(blog=blog_detail)

    return render(request, "blog/blog_detail.html", {"blog" : blog_detail , "reviews" : reviews})



def update_blog_view(request: HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.category = request.POST["category"]
        blog.content = request.POST["content"]
        blog.is_published = request.POST["is_published"]
        blog.published_at= request.POST["published_at"]
        blog.poster=request.FILES["poster"]
        blog.rating = request.POST["rating"]
        blog.save()

        return redirect('blog:blog_detail_view', blog_id=blog.id)

    return render(request, "blog/update.html", {"blog" : blog , "categories"  : Blog.categories})


def delete_blog_view(request: HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blog:read_blog_view")


def search_view (request: HttpRequest):
    
    if "search" in request.GET:
        keyword = request.GET["search"]
        blog = Blog.objects.filter(title__icontains=keyword)
    else:
        blog = Blog.objects.all()


    return render(request, "blog/search_page.html", {"blog" : blog})



def blog_category_view (request: HttpRequest):
    if "category" in request.GET and request.GET["category"] == "technology":
        blog = Blog.objects.filter(category__icontains="technology")

    elif "category" in request.GET and request.GET["category"] == "movies":
        blog = Blog.objects.filter(category__icontains="movies")

    elif "category" in request.GET and request.GET["category"] == "books":
        blog = Blog.objects.filter(category__icontains="books")

    elif "category" in request.GET and request.GET["category"] == "else":
        blog = Blog.objects.filter(category__icontains="else")
    else:
        blog = Blog.objects.all()

    blog_count = blog.count()

    return render(request, "blog/blog_home.html", {"blog" : blog, " blog_count" :  blog_count})


