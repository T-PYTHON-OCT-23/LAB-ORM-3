from django.urls import path
from . import views

app_name = "main"

urlpatterns = [ 
    path("",views.home_views, name="home_views")
    # path("add/", views.add_movie_view, name="add_movie_view"),
    # path("", views.movies_home_view, name="movie_home_view")

]