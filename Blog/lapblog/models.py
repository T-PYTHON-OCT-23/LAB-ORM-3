from django.db import models

# Create your models here.
class Web (models.Model):
   categories = models.TextChoices("Categories", ["Vlog", "Photoblog", "Blognews", "Personal blog"])
   Title = models.CharField(max_length=2048) 
   Contant =models.TextField()
   is_published =models.BooleanField()
   published_at = models.DateTimeField()
   category = models.CharField(max_length=64, choices=categories.choices , default="Vlog")
   poster = models.ImageField(upload_to="images/", default="images/r5.JPG")

class Review(models.Model):
   blog =  models.ForeignKey(Web,on_delete=models.CASCADE)
   full_name = models.CharField(max_length=512)
   comment = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)