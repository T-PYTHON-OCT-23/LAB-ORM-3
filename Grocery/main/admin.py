from django.contrib import admin
from .models import Product,Comment

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','description','price','quantity','brand','image','category')
    list_filter=('category',)

class CommentAdmin(admin.ModelAdmin):
    list_display=('product','name','content','rating','date')
    list_filter=('rating',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Comment,CommentAdmin)




# Register your models here.
