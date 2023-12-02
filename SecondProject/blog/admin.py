from django.contrib import admin
from .models import Blog , Review
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
 list_display = ('title', 'category', 'rating')

class ReviewAdmin(admin.ModelAdmin):
 list_display = ( 'blog', 'name', 'date', 'rating')


admin.site.register(Blog ,BlogAdmin)
admin.site.register(Review,ReviewAdmin )


