from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField(default=10)
    img=models.FileField(upload_to='image')