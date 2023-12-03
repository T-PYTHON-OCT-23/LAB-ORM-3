from django.contrib import admin
from .models import Blog, Review
# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display=('title','published_at','category',)
    list_filter=('category',)


admin.site.register(Blog,BlogAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display= ('user','date_add','rating',)
    list_filter=('blog',)

admin.site.register(Review,ReviewAdmin)
