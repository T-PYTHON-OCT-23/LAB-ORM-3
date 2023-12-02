from django.db import models

# Create your models here.

class Blog(models.Model):

    categories = models.TextChoices("categories" , ["Health" , "Stories" , "Science" ])

    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    category= models.CharField(max_length=50 , choices = categories.choices , default="Health")
    image = models.ImageField(upload_to="images/" , default="images/default.jpeg") 


    #لازم تكون جوا الكلاس .. تمثيل الاوبجكت كنص
    def __str__(self):
        return f"{self.title}"



class Review(models.Model):
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE)
    neme = models.CharField(max_length=512)
    comment=models.TextField()
    rating=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)


    #لازم تكون جوا الكلاس .. تمثيل الاوبجكت كنص
    def __str__(self):
        return f"{self.neme} : {self.comment}"