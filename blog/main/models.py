from django.db import models
from datetime import date


# Create your models here.


class Blog(models.Model):
    categories = models.TextChoices(
        "Categories", ["Coffee", "Tea", "Matcha", "Water"])

    name = models.CharField(max_length=512)
    paragraph = models.TextField(default='--')
    release_date = models.DateField(auto_now=True)
    category = models.CharField(
        max_length=2048, choices=categories.choices, default="Coffee")
    image = models.ImageField(upload_to="image/", default="image/default.jpg")


class Review(models.Model):
    Blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=512)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
