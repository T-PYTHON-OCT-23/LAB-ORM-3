from django.shortcuts import render ,redirect
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest
from .models import Blog, Review
# Create your views here.


def add_blogs_view(request:HttpRequest):
    if not request.user.is_staff:
        return render(request, 'main/not_authorized.html' , status=401)

    #Creating a new entry into the database for a movie
    msg = None
    try:
        if request.method == "POST":
            new_blogs = Blog(title=request.POST["title"], content=request.POST["content"], is_published = request.POST["is_published"], published_at = request.POST["published_at"], category=request.POST["category"],poster=request.FILES['poster'])
            new_blogs.save()
            return redirect("blogs:show_blogs_view")

        
        return render(request,"blogs/add.html", {"categories" : Blog.categories})
    except KeyError as e:
        return redirect("blogs:not_found_view")
    except Exception as e:
        msg = f"An error occured, please fill in all fields and try again . {e}"
    return render(request,"blogs/add.html", {"categories" : Blog.categories,  "msg" : msg})


        


def show_blogs_view(request:HttpRequest):
    
    blogs=Blog.objects.all()
    
    return render(request,"blogs/show_blogs.html", {"blogs" : blogs})

def not_found_view(request:HttpRequest):
        return render(request,"blogs/not_found.html")

def blog_detail_view(request:HttpRequest, blog_id):
    blog_detail = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        new_review = Review(blogg=blog_detail, full_name=request.POST["full_name"], rating=request.POST["rating"], comment=request.POST["comment"])
        new_review.save()
    try :
        blog = Blog.objects.get(id=blog_id)
        reviews = Review.objects.filter(blogg=blog)
        return render(request,"blogs/detail.html" , {"blog":blog, "reviews" : reviews})
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
        

    
def search_results_view(request: HttpRequest):

    if "search" in request.GET:
        keyword = request.GET["search"]
        blogs = Blog.objects.filter(title__contains=keyword)
    else:
        blogs = Blog.objects.all()


    return render(request, "blogs/search.html", {"blogs" : blogs}) 

def blogs_home_view_cat(request: HttpRequest, at):

    
    blogs = Blog.objects.filter(category=at)

    

    blogs_count = blogs.count()

    return render(request, "blogs/show_blogs.html", {"blogs" : blogs, "blogs_count" : blogs_count})


def home_view(request:HttpRequest):
    Reviews_last = Review.objects.all().order_by("-created_at")[0:5]
    blogs_last = Blog.objects.all().order_by("-published_at")[0:5]


    return render(request,"main/home.html",{"Reviews":Reviews_last ,"blogs":blogs_last})

def blog_view(request:HttpRequest):
    Reviews_last = Review.objects.all().order_by("-created_at")[0:5]
    blogs_last = Blog.objects.all().order_by("-published_at")[0:5]


    return render(request,"blogs/blog_home.html",{"Reviews":Reviews_last ,"blogs":blogs_last})