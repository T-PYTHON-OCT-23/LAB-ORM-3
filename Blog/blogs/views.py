from django.shortcuts import render ,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog ,Review



def read(request : HttpRequest):

    blogs=Blog.objects.all()

    return render(request, "blogs/read.html", {"blogs" : blogs})


def add(request : HttpRequest):

    if not request.user.is_staff:
     return render(request, 'main/not_authorized.html')
    
    msg = None
    
    if request.method=="POST":
        try:
            new_blog=Blog(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'],category=request.POST['category'])
            if "poster" in request.FILES:
             new_blog.poster =  request.FILES['poster']
            new_blog.save()
            return redirect("blogs:read")
    
        except Exception as e:
          msg = f"An error occured, please fill in all fields and try again . {e}"
    
    return render(request,'blogs/add.html', {"categories" : Blog.categories ,  "msg" : msg})



def detail(request:HttpRequest, blog_id):

    detail = Blog.objects.get(id=blog_id)

    if request.method=="POST":
     
        if not request.user.is_authenticated:
            return render(request, "main/not_authorized.html")
     
    new_review = Review(blog=detail, name=request.POST["name"], rating=request.POST["rating"],comment=request.POST["comment"])
    new_review.save()
    
    reviews = Review.objects.filter(blog=detail)

    return render(request, "blogs/detail.html", {"blog" : detail ,"reviews" : reviews})


def update(request : HttpRequest,blog_id):

    if not request.user.is_staff:
        return render(request, status=401)
    
    blog=Blog.objects.get(id=blog_id)
    
    if request.method=="POST":
        blog.title=request.POST['title']
        blog.content=request.POST['content']
        blog.is_published=request.POST['is_published']
        blog.published_at= request.POST["published_at"]
        blog.category=request.POST['category']
        blog.save()
       
        return redirect('blogs:detail',blog_id=blog.id)
    
    return render(request,'blogs/update.html',{"blog" : blog,'categories':Blog.categories})


def delete(request: HttpRequest, blog_id):
    if not request.user.is_superuser:
     
     return render(request,"main/not_authorized.html")

    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blogs:read")


def search(request: HttpRequest):
    if 'search' in request.GET:
        query = request.GET['search']
        blogs = Blog.objects.filter(title__contains=query)
    else:
         blogs = Blog.objects.all()   
    return render(request, 'blogs/search.html',  {"blogs" : blogs})


def BlogsCat(request : HttpRequest):

    if "category" in request.GET and request.GET["category"] =="Makeup":
      blogs = Blog.objects.filter(category__contains ="Makeup")

    elif "category" in request.GET and request.GET["category"] =="Movie":
        blogs = Blog.objects.filter(category__contains ="Movie")

    elif "category" in request.GET and request.GET["category"] =="Celebrities":
        blogs = Blog.objects.filter(category__contains ="Celebrities")

    elif "category" in request.GET and request.GET["category"] =="Care":
        blogs = Blog.objects.filter(category__contains ="Care")

    elif "category" in request.GET and request.GET["category"] =="Places":
        blogs = Blog.objects.filter(category__contains ="Places")    
    else:
        blogs = Blog.objects.all()
    return render(request ,"blogs/read.html" , {"blogs" : blogs})

