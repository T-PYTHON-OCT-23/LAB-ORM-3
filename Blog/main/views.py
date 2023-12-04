from django.shortcuts import render
from django.http import HttpRequest ,HttpResponse
from index.models import Sport,Review



# Create your views here.


def home_page_view (request : HttpRequest):
    comments=Review.objects.order_by('-created_at')[:6]
    return render(request,"main/home_page.html",{"comments":comments })