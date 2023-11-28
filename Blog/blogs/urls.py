from django.urls import path
from . import views
app_name = "blogs"
urlpatterns = [
    path('read/',views.read,name='read'),
    path('add/',views.add,name='add'),
    path("detail/<blog_id>/", views.detail, name="detail"),
    path("update/<blog_id>/", views.update, name="update"),
    path("delete/<blog_id>", views.delete, name="delete"),
    path('search/',views.search,name='search'),
    path("all/", views.BlogsCat, name="BlogsCat"),
    
]
