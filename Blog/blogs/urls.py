from . import views
from django.urls import path ,include


app_name = 'blogs'

urlpatterns = [
    path('add/',views.add_blogs_views,name='add_blogs_views'),
    path('',views.show_blogs_views,name='show_blogs_views'),
    path('detils/<mo_id>/', views.show_blogs_detils_view,name='show_blogs_detils_view'),
    path('update/<mo_id>/',views.update_blogs_views,name='update_blogs_views'),
    path('delete/blogs/<mo_id>',views.delete_blogs_views,name='delete_blogs_views'),
    path('filter/',views.filter_blogs_views,name='filter_blogs_views'),
    path('filter/search/',views.searchBar_blogs_views,name='searchBar_blogs_viewa'),
    path('movie/catagory/',views.filter_catagory_blogs_views,name='filter_catagory_blogs_views'),
    
]