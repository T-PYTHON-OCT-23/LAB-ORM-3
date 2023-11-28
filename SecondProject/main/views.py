from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import  Review ,Blog

# Create your views here.
def home_view(request: HttpRequest):
     
     latest_review = Review.objects.all().order_by("-date")[0:5]

     return render(request, "main/main.html" , {"latest_review": latest_review})

