from django.db import models

# Create your models here.

class Blogs(models.Model):
    categories = models.TextChoices("categories",["Action","Fantacy","Horror","Romantic"])

    title = models.CharField(max_length=2048)
    name_publisher = models.CharField(max_length=2048,null=True)
    published_location = models.CharField(max_length=1024,null=True)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField()
    catagory = models.CharField(max_length=1028,choices=categories.choices)
    images = models.ImageField(upload_to="images/",default="/images/mainlogo.png")

class Comment(models.Model):
    movie = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    rating_scale = models.IntegerChoices('rating_scall',['1','2','3','4','5'])

    name = models.CharField(max_length=1024)
    rating = models.IntegerField(max_length=512,choices=rating_scale.choices)
    content = models.TextField()
    create_ar = models.DateTimeField(auto_now_add=True)