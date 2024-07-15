from django.db import models

# Create your models here.
class img(models.Model):
    name=models.CharField(max_length=50)
    sal=models.FloatField(default=0)
    photo=models.ImageField(upload_to='image')
    date = models.DateTimeField(auto_now_add=True)