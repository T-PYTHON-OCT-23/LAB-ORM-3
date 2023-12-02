from django.contrib import admin
from .models import Blog , Review
# from django.contrib.auth.models import User



# # user = User.objects.create_user('','','')
# # user.save()

#custmization , to create col im admin page 
class BlogAdmin(admin.ModelAdmin):
    #display col
    list_display=('title' , 'category' , 'is_published' , 'published_at')
    #display after filttering , must write a  , if i want filter a single item 
    list_filter = ('category' , 'published_at' , 'is_published')

class ReviewAdmin(admin.ModelAdmin):
    list_display=('neme' , 'rating' , 'created_at' )
    list_filter = ('blog' , 'created_at')

# Register your models here.

admin.site.register(Blog , BlogAdmin)
admin.site.register(Review , ReviewAdmin)




