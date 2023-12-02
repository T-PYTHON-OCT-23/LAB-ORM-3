from django.db import models

# Create your models here.

class Info(models.Model):
    categories = models.TextChoices("Categories", ["Photo", "Video", "Other"])
    title = models.CharField(max_length=2000)
    contant = models.TextField()
    is_published= models.BooleanField()
    published_at = models.DateField()
    category = models.CharField(max_length=64, choices=categories.choices,default="Other")
    poster = models.ImageField(upload_to="images/", default="images/content.jpeg")

    def __str__(self) -> str:
        return f"{self.title}"
class Comment(models.Model):
    info=models.ForeignKey(Info , on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    like_it=models.BooleanField()
    Comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"