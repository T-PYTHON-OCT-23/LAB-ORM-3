from django.urls import path
from .import views

app_name ="accounts"

urlpatterns = [
    path('sign_in/',views.signin_view,name='signin'),
    path('sign_up/',views.signup_view,name='signup'),
    path('log_out/',views.log_out_user,name='log_out')
]