from django.urls import path
from . import views



app_name = "blogApp"

urlpatterns = [

    path("read/blog/" , views.read_blog_view , name="read_blog_view"),
    path("add/post" , views.add_post_view , name="add_post_view"),
    path("detail/<blog_id>/" , views.detail_blog_view , name="detail_blog_view"),
    path("update/<blog_id>/" , views.update_view , name="update_view"),
    path("delete/<blog_id>/" , views.delete_view , name="delete_view"),
    path("category/<item>/" , views.category_view , name="category_view"),
]