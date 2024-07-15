from django.contrib import admin

# Register your models here.
from uplodapp.models import img


class imgadmin(admin.ModelAdmin):
    list_display=['id','photo','date','name','sal']

admin.site.register(img,imgadmin)
