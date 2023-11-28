from django.db import models


class Blog(models.Model):

    categories = models.TextChoices("Categories", ["Technical", "News", "Marketing", "Entrepreneurship"])


    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateField()
    category = models.CharField(max_length=65, choices=categories.choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")


class Review(models.Model):
    ratings = models.TextChoices("Ratings", ["Excellent","Good", "Average", "Poor", "Very poor"])

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    summary = models.TextField()
    rating = models.CharField(max_length=80,choices=ratings.choices)
    published_at = models.DateTimeField(auto_now_add=True)