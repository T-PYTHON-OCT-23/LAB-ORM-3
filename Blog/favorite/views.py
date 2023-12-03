
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Favorite
from blogs.models import Blog
# Create your views here.


def add_favorite(request:HttpRequest, blog_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user")

    try:
        blog = Blog.objects.get(id=blog_id)
        user_favored = Favorite.objects.filter(user=request.user, blog=blog).first() 
        
        if not user_favored:
            new_favorite = Favorite(user=request.user, blog=blog)
            new_favorite.save()
        else:

            user_favored.delete()

        return redirect("blogs:detail", blog_id=blog.id)
    except Exception as e:
         return redirect("main:home")
    



def fav(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorite/fav.html', {"favorites" : favorites})