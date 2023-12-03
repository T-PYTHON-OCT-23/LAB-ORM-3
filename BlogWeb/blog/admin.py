from django.contrib import admin
from .models import Blog , Reviews
# Register your models here.
 
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','is_published','category')
    list_filter=('category',)





class ReviewsAdmin(admin.ModelAdmin):
    list_display=('name','rating','created_at')
    list_filter=('rating',)


admin.site.register(Blog,BlogAdmin)
admin.site.register(Reviews,ReviewsAdmin)