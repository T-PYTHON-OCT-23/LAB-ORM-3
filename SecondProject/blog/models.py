from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
        
    categories = models.TextChoices("Categories", ["technology", "movies", "books", "else"])

    title  = models.CharField(max_length=2048)
    content = models.TextField()
    is_published= models.BooleanField()
    published_at = models.DateField()
    category = models.CharField(max_length=64, choices=categories.choices)
    rating = models.IntegerField()
    poster = models.ImageField(upload_to="img/" , default="img/default.jpg")


class Review(models.Model):
    blog= models.ForeignKey(Blog , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete= models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    review= models.TextField()
    rating = models.IntegerField()

def __str__(self):
    return f"(self.title)"
