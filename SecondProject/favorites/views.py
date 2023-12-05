from django.shortcuts import render , redirect
from django.http import HttpRequest ,HttpResponse
from .models import Favorite
from blog.models import Blog

# Create your views here.


def add_favorite_view(request:HttpRequest, blog_id):

    if not request.user.is_authenticated:
        return redirect("account:sign_in_view")

    #add the favorite
    try:

        #1: get the movie
        blog = Blog.objects.get(id=blog_id)

        #2 : check if user already favored the movie
        user_favored = Favorite.objects.filter(user=request.user, blog=blog).first() #.first() bring the first Favorite object if exists else None
        
        if not user_favored:
            #3 : add the favorite
            new_favorite = Favorite(user=request.user, blog=blog)
            new_favorite.save()
        else:
            #or delete it if already exists
            user_favored.delete()

        return redirect("blog:blog_detail_view", blog_id=blog.id)
    except Exception as e:
        return redirect("main:home_view")
    


def my_favorites_view(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorites/fav_display.html', {"favorites" : favorites})




