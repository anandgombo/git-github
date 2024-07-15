from django.urls import path

from . import views

app_name='core'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.course,name='contact'),    
    path('signup/',views.signup,name='signup'),
    path('login/', views.login_view, name='login'),
    
]
