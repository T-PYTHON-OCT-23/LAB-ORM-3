from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog, Review

def add_blog_view(request: HttpRequest):
    if not request.user.is_staff:
        return render(request, 'main/not_authorized.html' , status=401)

    msg = None
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST["content"], is_published=request.POST["is_published"], published_at=request.POST["published_at"],category=request.POST["category"],image=request.FILES["image"])
        new_blog.save()

        return redirect("blogs:blogs_home_view")

    return render(request, "blogs/add.html", {"categories" : Blog.categories, "msg": msg})



def blogs_home_view(request: HttpRequest):
    blogs = Blog.objects.all()

    return render(request, "Blogs/blogs_home.html", {"blogs" : blogs})


def blogs_details_view(request:HttpRequest, blog_id ):

    blog_detail = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        new_review = Review(blog=blog_detail, author_name=request.POST["author_name"], title=request.POST["title"], summary=request.POST["summary"], rating=request.POST["rating"])  
        new_review.save()

    reviews = Review.objects.filter(blog=blog_detail)  
    
    return render(request , "blogs/blogs_details.html", {"blog_detail":blog_detail , "reviews" : reviews})



def not_exist(request:HttpRequest):
    return render(request,"blogs/not_exist.html")


def update_blog_view(request: HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        if request.method == "POST":
            blog.title = request.POST["title"]
            blog.content = request.POST["content"]
            blog.is_published = request.POST["is_published"]
            blog.published_at = request.POST["published_at"]
            blog.category = request.POST["category"]
            blog.save()

            return redirect('blogs:blogs_details_view', blog_id=blog.id)
    except Exception as e:
        return render(request,"blogs/not_exist.html")


    return render(request, "blogs/update_blog.html", {"blog" : blog, "categories": Blog.categories})


    
def delete_blog_view(request:HttpRequest,blog_id):

    blog= Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blogs:blogs_home_view")


def search_page_view(request:HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        blogs = Blog.objects.filter(title__contains=keyword)
    else:
        blogs = Blog.objects.all()

    return render(request,"blogs/search_page.html", {"blogs": blogs})


def blogs_home_view_cat(request:HttpRequest, cate):

    blogs = Blog.objects.filter(category=cate).order_by("published_at")
    blogs_count = blogs.count()

    return render(request, "blogs/blogs_home.html", {"blogs" : blogs, "blogs_count" : blogs_count})




def add_review_view(request: HttpRequest, blog_id):

    if request.method == "POST":

        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html", status=401)

        blog_obj = Blog.objects.get(id=blog_id_id)
        new_review = Review(blog=blog_obj,  full_name=request.POST["full_name"], rating=request.POST["rating"], comment=request.POST["comment"])  
        new_review.save()
        return redirect("blogs:blog_detail_view", movie_id=movie_obj.id)