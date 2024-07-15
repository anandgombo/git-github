from django.db import models

# Create your models here.from django.db import models

    

class Category(models.Model):
    name=models.CharField(max_length=50)
    des=models.CharField(max_length=100) 

class Productcard(models.Model):
    name=models.CharField(max_length=50)
    des=models.CharField(max_length=100) 
    img=models.FileField(upload_to='image1')

class Product(models.Model):
    name=models.CharField(max_length=50)
    des=models.CharField(max_length=100) 
    img=models.FileField(upload_to='image')

    def __str__(self):
        return self.name