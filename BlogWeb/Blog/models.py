from django.db import models
 

class Blog1(models.Model):
    categories=models.TextChoices('categories',['Food','Travel','Fashion','Personal'])
    title=models.CharField(max_length=2000)
    content=models.TextField()
    is_published=models.BooleanField()
    published_at=models.DateField()
    category=models.CharField(max_length=200,choices=categories.choices)
    image= models.ImageField(upload_to="images/", default="images/blog.jpeg")
        # Create your models here.

class Comment(models.Model):
    blog=models.ForeignKey(Blog1,on_delete=models.CASCADE)
    name=models.CharField(max_length=1000)
    content=models.TextField()
    rating=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
