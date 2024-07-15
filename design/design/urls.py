"""
URL configuration for design project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun1,name='home'),
    path('login/',views.fun3,name='login'),
    path('cats/',views.fun2,name='cats'),    
    path('addprod/',views.Product1,name='addprod'),
    path('addcats/',views.Categoryp,name='addcats'),   
      
    path('cardprod/',views.cardprod,name='cardprod'),    
    path('datadisp/',views.datadisp,name='datadisp'),     
    path('buyproduct/<int:product_id>/', views.buyproduct, name='buyproduct'),
    path('buyproduct<int:product_id>/', views.buyproduct, name='buyproduct'),
    path('editproduct<int:product_id>/', views.edit_product, name='edit_product'),
    path('deleteproduct<int:product_id>/', views.delete_product, name='deleteproduct'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
