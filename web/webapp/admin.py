
from django.contrib import admin
from .models import Item
# Register your models here.
class adminitem(admin.ModelAdmin):
    list_display=('name','price','description','image')
admin.site.register(Item,adminitem)