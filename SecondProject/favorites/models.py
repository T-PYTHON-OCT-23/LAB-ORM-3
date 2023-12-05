from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

# Create your models here.

class Favorite(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.username} favored {self.blog.title}"