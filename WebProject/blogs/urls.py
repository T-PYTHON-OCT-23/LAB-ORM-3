from django.urls import path
from . import views
app_name = "blogs"

urlpatterns = [
    path("", views.blogs_home_view, name="blogs_home_view"),
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("detail/<blog_id>/", views.blogs_details_view, name="blogs_details_view"),
    path("not_exsit/", views.not_exist, name="not_exist" ),
    path("update/<blog_id>/", views.update_blog_view , name="update_blog_view"),
    path("delete/<blog_id>/", views.delete_blog_view, name="delete_blog_view"),
    path("search/",views.search_page_view , name="search_page_view"),
    path("category/<cate>/", views.blogs_home_view_cat, name="blogs_home_view_cat"),
]


