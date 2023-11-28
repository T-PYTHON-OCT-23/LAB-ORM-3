from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from post.models import Review
# Create your views here.

def home_view(request: HttpRequest):

    review =Review.objects.all().order_by("-created_at")[0:5]

    return render(request, "main/index.html" , {"review" : review})
