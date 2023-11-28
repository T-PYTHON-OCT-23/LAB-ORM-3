from django.shortcuts import render  , redirect
from django.http import HttpRequest , HttpResponse
from blogApp.models import Review , Blog

# Create your views here.


def home_view(request: HttpRequest):
    
    reviews=Review.objects.all().order_by("created_at")

    return render(request , "main/home.html" , {"reviews" : reviews})



def delete_comment_view(request :HttpRequest , comment):
    deleted_comment=Review.objects.get(id = comment)

    deleted_comment.delete()

    return redirect("main:home_view" )
