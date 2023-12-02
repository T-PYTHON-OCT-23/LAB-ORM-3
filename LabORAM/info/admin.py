from django.contrib import admin
from . models import Info,Comment
# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display=('title','is_published','published_at','category','poster')
    list_filter=('category',)

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','info', 'like_it', 'created_at')
    list_filter=('info',)
admin.site.register(Info,InfoAdmin)
admin.site.register(Comment, CommentAdmin)