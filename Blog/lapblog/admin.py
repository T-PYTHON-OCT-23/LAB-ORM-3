from django.contrib import admin
from .models import Web, Review # اسماء المودل اللي عندي واللي ابغى اضيفها للوحة التحكم للادمن

# Register your models here.
class WebAdmin(admin.ModelAdmin):

    list_display = ('Title', 'is_published')
    list_filter = ('category',)


class ReviewModel(admin.ModelAdmin):
    list_display = ('full_name', 'blog', 'comment', 'created_at')
    list_filter = ('blog',)

admin.site.register(Web, WebAdmin)
admin.site.register(Review, ReviewModel)