from django.db import models

# Create your models here.
class singup(models.Model):
    name=models.CharField(max_length=40,)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    password=models.CharField(max_length=25)
    compass=models.CharField(max_length=25)
    

