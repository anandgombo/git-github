from django.db import models

# Create your models here.
class Customer(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    father=models.CharField(max_length=100)
    email=models.EmailField()
    pass1=models.CharField(max_length=20)
    Phone=models.CharField(max_length=10)
    
class Category(models.Model):
    name=models.CharField(max_length=50)
    des=models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    des=models.CharField(max_length=100)
    image=models.FileField(upload_to='uploads/products/')       