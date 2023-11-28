from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Published,Comment
# Create your views here.

def add_blog(request:HttpRequest):
    
    if request.method == 'POST':
        
        try:
            new_published = Published(title=request.POST['title'],content =request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'],image = request.FILES["image"],blog_content=request.POST["blog_content"])
            
            new_published.save()
        except Exception:
            return redirect('blog_op:add_blog')
    
        return redirect('blog_op:publications')

    return render (request,'blog_op/add.html',{"blog_content": Published.blogs_content})

def publications(request:HttpRequest):
    
    if 'search' in request.GET:
        search_value = request.GET['search']
        pub = Published.objects.filter(blog_content=search_value)
    else: pub = Published.objects.all()
    
    
    
    return render(request,'blog_op/publications.html',{'publications':pub,"blog_content": Published.blogs_content})



def published_detail(request:HttpRequest,published_id):
    
    pub = Published.objects.get(id=published_id)

    if request.method == 'POST':
        new_comment = Comment(published=pub,name=request.POST['name'],comment=request.POST['comment'])
        new_comment.save()
    
    replies=Comment.objects.filter(published=pub) 
    return render(request,'blog_op/detail.html',{'published':pub,"replies":replies})

def update(request:HttpRequest,published_id):
    published = Published.objects.get(id=published_id)
    if request.method == 'POST':
        published.title = request.POST["title"]
        published.content =request.POST['content']
        published.published_at=request.POST['published_at']
        published.blog_content = request.POST['blog_content']
        published.image = request.FILES["image"]
        published.save()
        redirect('blog_op:publications')
        
    return render(request,'blog_op/update.html',{'update':published,"blog_content": Published.blogs_content})



def delete_blog(request:HttpRequest,published_id):
    
    published = Published.objects.get(id=published_id)
    published.delete()
    
    return redirect('blog_op:publications')


def search(request:HttpRequest):
    if "search" in request.GET:
        search_value = request.GET['search']
        pup =Published.objects.filter(title__contains=search_value)
    else:
        pup = Published.objects.all() 
    return render(request,"blog_op/search.html",{'search':pup})
