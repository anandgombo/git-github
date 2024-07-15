from django.contrib import admin
from myapp.models import User
# Register your models here.
class admindata(admin.ModelAdmin):
    list_display=('id','name','email','password','img')
admin.site.register(User,admindata)