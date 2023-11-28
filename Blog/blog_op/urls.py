from django.urls import path
from .import views

app_name = 'blog_op'

urlpatterns =[
    path('add/',views.add_blog,name='add_blog'),
    path('publications/',views.publications,name='publications'),
    path('puplidhed/<published_id>/',views.published_detail,name='published_detail'),
    path('update/<published_id>/',views.update,name='update'),
    path('delete/<published_id>/',views.delete_blog,name='delete_blog'),
    path("search/",views.search,name='search')
]