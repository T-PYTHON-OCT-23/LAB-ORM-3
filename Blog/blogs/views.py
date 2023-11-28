from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Blog , Comment
# Create your views here


def add_blogs_view(request:HttpRequest):
    try:
        if request.method == "POST":
            new_blogs = Blog(title=request.POST["title"], content=request.POST["content"], is_published = request.POST["is_published"], published_at = request.POST["published_at"], category=request.POST["category"])
            if "poster" in request.FILES:
                new_blogs.poster = request.FILES["poster"]
            new_blogs.save()
            return redirect("blogs:show_blogs_view")

        
        return render(request,"blogs/add.html", {"categories" : Blog.categories})
    except Exception as e:
        return redirect("blogs:not_found_view")
        


def show_blogs_view(request:HttpRequest):
    
    blogs=Blog.objects.all()
    
    if "filter" in request.GET and request.GET["filter"]=="Political":
        blogs = Blog.objects.filter(category="Political")
    elif "filter" in request.GET and request.GET["filter"]=="Sports":
        blogs = Blog.objects.filter(category="Sports")
    elif "filter" in request.GET and request.GET["filter"]=="Social":
        blogs = Blog.objects.filter(category="Social")
    elif "filter" in request.GET and request.GET["filter"]=="Technical":
        blogs = Blog.objects.filter(category="Technical")

    if "search" in request.GET:
        search = request.GET["search"]
        blogs = Blog.objects.filter(title__contains=search)
        
        
    return render(request,"blogs/show_blogs.html", {"blogs" : blogs})

def not_found_view(request:HttpRequest):
        return render(request,"blogs/not_found.html")

def home_view(request:HttpRequest):
    comments_last = Comment.objects.all().order_by("-created_at")[0:5]
    blogs_last = Blog.objects.all().order_by("-published_at")[0:5]

    
    return render(request,"main/home.html",{"comments":comments_last ,"blogs":blogs_last})


def blog_detail_view(request:HttpRequest, blog_id):
    
    try:
        
        blog = Blog.objects.get(id=blog_id)
        
        if request.method == "POST":
            new_comment = Comment(blog=blog , name=request.POST["name"], comment = request.POST["comment"])
            new_comment.save()
            
        
        comments = Comment.objects.filter(blog=blog)
            
        return render(request, "blogs/detail.html" , {"blog" : blog, "comments" : comments})
    except Exception as e:
        return redirect("blogs:not_found_view")
    
    
    
def blog_update_view(request:HttpRequest, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        if request.method == "POST":
                blog.title = request.POST["title"]
                blog.content = request.POST["content"]
                blog.is_published = request.POST["is_published"]
                blog.published_at =request.POST["published_at"]
                blog.category = request.POST["category"]
                blog.poster = request.FILES["poster"]
                blog.save()
            
                return redirect('blogs:blog_detail_view',blog_id=blog_id)
        return render(request,"blogs/update.html", {"blog" : blog, "categories"  : Blog.categories})
    except Exception as e :
        return redirect("blogs:not_found_view")



def blog_delete_view(request:HttpRequest, blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog.delete()
        return redirect("blogs:show_blogs_view")
        

    
    
