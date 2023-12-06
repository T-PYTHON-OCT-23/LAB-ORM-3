from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Favorite
from post.models import Blog 
# Create your views here.

def add_favorite_view(request:HttpRequest, post_id):

    if not request.user.is_authenticated:
        return redirect("accounts:login_user")

    try:

        # get the post
        post = Blog.objects.get(id=post_id)

        #2 : check if user already favored the post
        user_favored = Favorite.objects.filter(user=request.user, post=post).first() 
        
        if not user_favored:
            #3 : add the favorite
            new_favorite = Favorite(user=request.user, post=post)
            new_favorite.save()
        else:
            #or delete it if already exists
            user_favored.delete()

        return redirect("post:post_detail_view", post_id=post.id)
    except Exception as e:
        return redirect("main:home_view")
    

def my_favorites_view(request: HttpRequest):

    favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'favorites/favorites.html', {"favorites" : favorites})

