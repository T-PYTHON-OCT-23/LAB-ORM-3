from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/",views.user_registeration_view,name="user_registeration_view"),
    path("login/",views.user_log_in_view,name="user_log_in_view"),
    path("logout/",views.user_log_out_view,name="user_log_out_view"),
]