from django.shortcuts import render
from django.http import HttpRequest
from blog_op.models import Comment
from datetime import date
# Create your views here.

def home (request:HttpRequest):
   date_now = date.today()
   latest_comment=Comment.objects.filter(commented_at__contains=date_now).order_by('-commented_at')[0:5]
   return render(request,'main/home.html',{'comments':latest_comment})

