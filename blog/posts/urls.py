from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [ 
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("", views.post_home_view, name="post_home_view"),
    path("detail/<posts_id>/", views.post_detail_view, name="post_detail_view"),
    path("update/<posts_id>/", views.update_post_view, name="update_post_view"),
    path("delete/<posts_id>", views.delete_post_view, name="delete_post_view"),
    path("category/<item>/", views.display_Blog_views, name="display_Blog_views"),

]