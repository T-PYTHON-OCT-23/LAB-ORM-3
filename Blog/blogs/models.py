from django.db import models

# Create your models here.

class Blog(models.Model):
    categories = models.TextChoices("Categories", ["Dialogues", "Articles", "Stories", "Fantasy"])
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    published_at = models.DateField()
    category = models.CharField(max_length=64, choices=categories.choices)
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")


class Review(models.Model):
    blogg =  models.ForeignKey(Blog, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=512)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    