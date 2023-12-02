from django.db import models

class Product(models.Model):
    categories=models.TextChoices('categories',['Dairy','PantryStaples','Snacks','Candy','Bakery','Beverages','Chocolate'])
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    brand=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images/")
    category=models.CharField(max_length=200,choices=categories.choices)

class Comment(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    name=models.CharField(max_length=1000)
    content=models.TextField()
    rating=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    
