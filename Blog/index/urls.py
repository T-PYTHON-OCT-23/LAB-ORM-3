from django.urls import path
from . import views

app_name = "index"

urlpatterns = [
    path("add/",views.add_view,name="add_view"),
    path("",views.home_view,name="home_view"),
    path("details/<sport_id>/",views.details_view,name="details_view"),
    path("update/<sport_id>/",views.update_view,name="update_view"),
    path("delete/<sport_id>/",views.delet_view,name="delet_view"),
    path("review/add/<sport_id>/",views.add_review_view,name="add_review_view"),
]