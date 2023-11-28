from django.urls import path
from . import views 

app_name = "main"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/details/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/update/<int:pk>/', views.post_update, name='post_update'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/comment/<int:pk>/', views.add_comment, name='add_comment'),

]