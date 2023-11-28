from django.urls import path
from . import views

app_name = "lapblog"

urlpatterns = [ 
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("", views.blog_home_view, name="blog_home_view"),
    path("detail/<blog_id>/", views.blog_detail_view, name="blog_detail_view"),
    path("update/<blog_id>/", views.update_blog_view, name="update_blog_view"),
    path("delete/<blog_id>", views.delete_blog_view, name="delete_blog_view"),
    path("search", views.search_blog_view, name="search_blog_view"),
    path("category/<cat>/", views.blog_home_view_cat, name="blog_home_view_cat")

  ]