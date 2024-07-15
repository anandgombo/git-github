from django.contrib import admin

# Register your models here.
from app.models import Category,Product,Productcard
class adminacts(admin.ModelAdmin):
    list_display=('name','des')

admin.site.register(Category,adminacts)


class adminprod(admin.ModelAdmin):
    list_display=('name','des','img')

admin.site.register(Product,adminprod)


class adminprodcard(admin.ModelAdmin):
    list_display=('name','des','img')

admin.site.register(Productcard,adminprodcard)