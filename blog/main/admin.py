from django.contrib import admin
from .models import Blog, Review

# Register your models here.


class BlogAdmin(admin.ModelAdmin):

    list_display = ('name', 'release_date', 'category')
    list_filter = ('name', 'category')


class ReviewModel(admin.ModelAdmin):
    list_display = ('full_name', 'Blog', 'rating', 'comment', 'created_at')
    list_filter = ('Blog', 'rating')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Review, ReviewModel)
