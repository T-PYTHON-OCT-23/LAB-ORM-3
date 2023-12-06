from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("logout/", views.logout_user, name="logout_user"),
    path("test/",views.test_page,name=""),
    path("profile/<user_id>/", views.user_profile_view, name="user_profile_view"),
    path("update/", views.update_user_view, name="update_user_view")
]