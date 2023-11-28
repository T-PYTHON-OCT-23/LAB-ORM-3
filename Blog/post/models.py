from django.db import models

# Create your models here.

class Blog(models.Model):

    categories = models.TextChoices("Categories", ["Educationl", "Art", "Cultual", "Podcast" ,"Corporate"])
   
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField()
    category = models.CharField(max_length=70, choices=categories.choices, default="Cultural" )
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")



class Review(models.Model):
    post =  models.ForeignKey(Blog, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=700)
    rating = models.TextField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)