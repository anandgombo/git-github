"""
URL configuration for gpt project.

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
from gptapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('case_list/', views.case_list, name='case-list'),
    path('add_case/', views.add_case, name='add-case'),
    path('update/<int:pk>/', views.update_case, name='update-case'),
    path('delete/<int:pk>/', views.delete_case, name='delete-case'),
    
]
