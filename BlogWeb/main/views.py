from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from Blog.models import Comment
# Create your views here.
#source venv/Scripts/activate
def home_page(request : HttpRequest):
    comments=Comment.objects.all().order_by('-date')[0:5]

    return render(request,'main/home.html',{'comments':comments})

