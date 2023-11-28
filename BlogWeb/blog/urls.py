from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [ 
    path("add/",views.add_blog_views, name="add_blog_views"),
    path("", views.home_blog_views, name="home_blog_views"),
    path("details/<blog_id>/", views.details_blog_views, name="details_blog_views"),
    path("delete/rev/<rev_id>/", views.delete_rev_views ,name="delete_rev_views"),
    path("updated/<blog_id>/", views.updated_blog, name="updated_blog"),
    path("delete/<blog_id>/", views.delete_blog_views ,name="delete_blog_views"),
    path('search/', views.search_blog_views, name="search_blog_views")
   # path('category/<item>',views.home_views_category,name="home_views_category")
]