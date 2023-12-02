from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register_user_page, name="register_user_page"),
    path("login/", views.login_user_page, name="login_user_page"),
    path("logout/", views.logout_user_page, name="logout_user_page")
]