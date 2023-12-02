from django.contrib import admin

from .models import  Blog, Review

# Register your models here.

class BlogAdmin(admin.ModelAdmin):

    list_display=('title','category','poster')
    list_filter=('category', )


class ReviewModel(admin.ModelAdmin):    

    list_display=('full_name', 'post','comment')
    list_filter = ('post','rating' )

admin.site.register(Blog,BlogAdmin)
admin.site.register(Review, ReviewModel)     