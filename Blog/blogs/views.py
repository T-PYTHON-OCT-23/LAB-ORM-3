from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Blogs,Comment
from datetime import date
# Create your views here.

def add_blogs_views(request:HttpRequest):

    if request.method == 'POST':
        new_blogs = Blogs(title=request.POST['title'],content=request.POST['content'],is_published=request.POST['is_published'],published_at=request.POST['published_at'],name_publisher=request.POST['name_publisher'],published_location=request.POST['published_location'],catagory=request.POST['catagory'],images=request.FILES['images'])
        new_blogs.save()
        
        return redirect('blogs:show_blogs_views')
    
    return render(request, 'blogs/add_blogs.html',{'catagory':Blogs.categories.choices})

def show_blogs_views(request:HttpRequest):
    today_date = date.today()
    blogs = Blogs.objects.all()
    #.filter(is_published=True)
    commento = Comment.objects.all().filter(create_ar__contains=today_date).order_by('-create_ar')[0:5]

    return render(request, 'blogs/show_blogs.html',{'blogs':blogs,'catagory':Blogs.categories.choices,'comment':commento})

def filter_blogs_views(request:HttpRequest):
    if request.method == 'POST':
        f = request.POST['filter']
        b = Blogs.objects.all().filter(is_published=f)

        return  render(request, 'blogs/show_blogs.html',{'blogs':b})

def filter_catagory_blogs_views(request:HttpRequest):
    if request.method == 'POST':
        f = request.POST['catagory']
        b = Blogs.objects.all().filter(catagory=f)

        return  render(request, 'blogs/show_blogs.html',{'blogs':b})
    
def searchBar_blogs_views(request:HttpRequest):

    if request.GET:
        f = request.GET['search']
        b = Blogs.objects.all().filter(title__contains=f)

        return  render(request, 'blogs/filter_blogs.html',{'blogs':b})
    
def show_blogs_detils_view(request:HttpRequest,mo_id):

    if request.method == 'POST':
        f = Blogs.objects.get(id=mo_id)
        new_comment = Comment(movie=f,name=request.POST['name'],rating=request.POST['rating'],content=request.POST['content'])
        new_comment.save()
        return redirect('blogs:show_blogs_views')

    try:
        movie = Blogs.objects.get(id=mo_id)
        commento = Comment.objects.filter(movie=mo_id)
        return render(request, 'blogs/show_blogs_detlies.html',{'blogs':movie,'rating':Comment.rating_scale.choices,'commento':commento})
    except Exception as e:
        #return redirect('blogs:show_blogs_views')
        print(e)

def update_blogs_views(request:HttpRequest,mo_id):

    blogs = Blogs.objects.get(id=mo_id)
    if request.method == 'POST':
        blogs.title = request.POST['title']
        blogs.name_publisher = request.POST['name_publisher']
        blogs.published_location = request.POST['published_location']
        blogs.content = request.POST['content']
        blogs.is_published = request.POST['is_published']
        blogs.published_at = request.POST['published_at']
        blogs.images = request.FILES['images']
        blogs.catagory = request.POST['catagory']
        blogs.save()
        return redirect('blogs:show_blogs_detils_view',mo_id=blogs.id)

    return render(request,'blogs/update_blogs.html',{'blogs':blogs,'cat':Blogs.categories.choices})

def delete_blogs_views(request:HttpRequest,mo_id):
    blogs = Blogs.objects.get(id=mo_id)
    blogs.delete()
    
    return redirect('blogs:show_blogs_views')