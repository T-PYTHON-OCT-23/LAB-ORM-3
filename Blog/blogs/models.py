from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    
    categories=models.TextChoices("Categories", ["Makeup", "Movie","Celebrities", "Care","Places"])
  

    title=models.CharField(max_length=100)
    content=models.TextField()
    is_published=models.BooleanField()
    published_at=models.DateField()
    category=models.CharField(max_length=50,choices=categories.choices,)
    poster = models.ImageField(upload_to="images/", default="images/blog.jpg")

    def __str__(self):
        return f"{self.title}"

class Review(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_add= models.DateTimeField(auto_now_add=True)
    rating= models.TextField()
    comment = models.TextField()

    def __str__(self):
     return f"{self.user} : {self.blog}"