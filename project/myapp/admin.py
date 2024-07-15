from django.contrib import admin
from myapp.models import data
# Register your models here.
class admindata(admin.ModelAdmin):
    list_display=('id','name','roll','img')
admin.site.register(data,admindata)