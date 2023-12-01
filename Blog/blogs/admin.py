from django.contrib import admin
from .models import Blog , Review


class BlogAdmin(admin.ModelAdmin):
    list_filter = ('category','title')
    list_display = ('content','category','title',)

class ReviewAdmin(admin.ModelAdmin):
    list_filter = ('blogg',)
    list_display = ('blogg','full_name','rating',)


admin.site.register(Review,ReviewAdmin)
admin.site.register(Blog,BlogAdmin)