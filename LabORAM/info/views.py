from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Info , Comment

# Create your views here.



def add_info_view(request: HttpRequest):

    #Creating a new entry into the database for a info

    if request.method == "POST":
        new_info = Info(title=request.POST["title"], contant=request.POST["contant"], is_published=request.POST["is_published"], published_at=request.POST["published_at"],category=request.POST["category"], poster=request.FILES["poster"])
        new_info.save()

        return redirect("info:info_home_view")

    return render(request, "info/add.html", {"categories" : Info.categories})



def info_home_view(request: HttpRequest):
    if "title" in request.GET:
        keyword =request.GET.get("title")
        print(keyword)
        info = Info.objects.filter(title__contains=keyword)
    elif "category"in request.GET and request.GET["category"]== "Photo":
        info = Info.objects.filter(category="Photo")
    elif "category"in request.GET and  request.GET["category"]== "Video":
        info = Info.objects.filter(category="Video")
    elif "category"in request.GET and  request.GET["category"]== "Other":
        info = Info.objects.filter(category="Other")
    else:
        info= Info.objects.all()
    comment=Comment.objects.all().order_by("-created_at")[0:5]

    return render(request, "info/info_home.html", {"info" : info,"comment":comment})

    
        
def info_details_view(request: HttpRequest,info_id):

    
    info = get_object_or_404(Info,id=info_id)
    if request.method == "POST":
        comment1=Comment(info=info , name=request.POST["name"] ,like_it=request.POST["like_it"] , Comment=request.POST["comment"])
        comment1.save()
    comment2=Comment.objects.filter(info=info).order_by("-created_at")
    
    return render(request, "info/info_details.html", {"info" : info, "comment2":comment2})



def update_info_view(request: HttpRequest, info_id):

    info = Info.objects.get(id=info_id)

    if request.method == "POST":
        info.title = request.POST["title"]
        info.contant = request.POST["contant"]
        info.published_at = request.POST["published_at"]
        info.poster=request.FILES["poster"]
        info.category = request.POST["category"]
        info.save()

        return redirect('info:info_details_view', info_id=info.id)

    return render(request, "info/update.html", {"info" : info,"categories"  : Info.categories})


def delete_info_view(request: HttpRequest, info_id):

    info = Info.objects.get(id=info_id)
    info.delete()

    return redirect("info:info_home_view")
