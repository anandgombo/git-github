
from django.core import validators
from django import forms
from myapp.models import User

class form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'image']
