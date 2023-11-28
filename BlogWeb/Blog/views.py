from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog1,Comment
# Create your views here.

def read_blog(request : HttpRequest):
    blogs=Blog1.objects.all()
    return render(request, "Blog/read_blog.html", {"blogs" : blogs})

def add_blog(request : HttpRequest):
    if request.method=="POST":
        new_blog=Blog1(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'],category=request.POST['category'],image=request.FILES['image'])
        new_blog.save()
        return redirect("Blog:read_blog")
    return render(request,'Blog/add_blog.html',{"categories" : Blog1.categories})

def blog_detail(request : HttpRequest,blog_id):
    try:
        blog=Blog1.objects.get(id=blog_id)
        if request.method=='POST': 
            new_comment=Comment(blog=blog,name=request.POST['name'],content=request.POST['content'],rating=request.POST['rating'])
            new_comment.save()
        comments=Comment.objects.filter(blog=blog)
    except Exception as e :
        return render(request,'Blog/not_exist.html')
    return render(request,'Blog/blog_detail.html',{'blog':blog,'comments':comments})


def not_exist(request : HttpRequest):
    return render(request,'Blog/not_exist.html')

def update_blog(request : HttpRequest,blog_id):
    blog=Blog1.objects.get(id=blog_id)
    if request.method=="POST":
        blog.title=request.POST['title']
        blog.content=request.POST['content']
        blog.is_published=request.POST['is_published']
        blog.published_at=request.POST['published_at']
        blog.category=request.POST['category']
        blog.image=request.FILES['image']
        blog.save()
        return redirect('Blog:blog_detail',blog_id=blog.id)
    return render(request,'Blog/update_blog.html',{"blog" : blog,'categories':Blog1.categories})

def delete_blog(request: HttpRequest, blog_id):
    blog = Blog1.objects.get(id=blog_id)
    blog.delete()

    return redirect("Blog:read_blog")

def search_page(request: HttpRequest):
    
    if 'search' in request.GET:
        search_term = request.GET['search']
        blogs = Blog1.objects.filter(title__contains=search_term)
    else:
        blogs = Blog1.objects.all()
    return render(request,'Blog/search_page.html',{'blogs':blogs})

def category_blog(request: HttpRequest,cat):
    blogs=Blog1.objects.filter(category=cat).order_by('published_at')
    return render(request,'Blog/search_page.html',{'blogs':blogs})