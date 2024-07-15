from django.contrib import admin
from app6.models import singup
# Register your models here.
class adminsingup(admin.ModelAdmin):
    
    list_display=('name','email','phone','password','compass')

admin.site.register(singup,adminsingup)