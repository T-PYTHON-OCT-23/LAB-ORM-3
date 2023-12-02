from django.contrib import admin

from .models import Blog, Review



#to customize the display table in the admin panel (optional)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'content', 'is_published', 'published_at','category')



class ReviewModel(admin.ModelAdmin):
    list_display = ('author_name', 'title', 'summary', 'rating','published_at')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Review, ReviewModel)


