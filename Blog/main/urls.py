from django.urls import path
from . import views



app_name = "main"

urlpatterns = [
path("", views.home_view , name="home_view"),
path("delete/comment/<comment>/" , views.delete_comment_view , name="delete_comment_view"),
path("eror/" , views.eror_view , name="eror_view"),


]