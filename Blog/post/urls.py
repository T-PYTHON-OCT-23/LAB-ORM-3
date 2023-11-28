from django.urls import path
from . import views

app_name = "post"

urlpatterns = [ 
    path("", views.display_blog_view, name="display_blog_view"),
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("not/", views.not_exist_view, name="not_exist_view"),
    path("detail/<post_id>/", views.post_detail_view, name="post_detail_view"),
    path("update/<post_id>/", views.update_post_view, name="update_post_view"),
    path("delete/<post_id>", views.delete_post_view, name="delete_post_view"),
    path("search/", views.search_post_view, name="search_post_view"),
    path("category/<cat>/", views.display_blog_view_cat, name="display_blog_view_cat")
]
