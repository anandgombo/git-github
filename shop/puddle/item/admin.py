from django.contrib import admin

# Register your models here.
from .models import Category,Item
admin.site.register(Category)

class adminItem(admin.ModelAdmin):
    list_display=( 'id','category','name','description','price','image','is_sold','created_at')
admin.site.register(Item,adminItem)