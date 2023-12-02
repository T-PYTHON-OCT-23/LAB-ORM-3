from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('add/product/',views.add_page,name='add_page'),
    path('browse/product/',views.browse_page,name='browse_page'),
    path('detail/<product_id>/',views.detail_page,name='detail_page'),
    path('delete/product/<product_id>/',views.delete_product,name='delete_product'),
    path('update/product/<product_id>/',views.update_page,name='update_page'),
    path('not/exist/',views.not_exist,name='not_exist'),
    path('search/',views.search_page,name='search_page'),
    path('category/<cat>/',views.category_view,name='category_view'),
    
    
]