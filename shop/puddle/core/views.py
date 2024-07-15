from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from item.models import Category,Item
from . forms import SingupForm,LoginForm
# Create your views here.
def index(request):
    item=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,"core/index.html",{
        'categories':categories,'items':item
    })

def course(request):
    return render(request,"core/course.html")

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SingupForm()
    return render(request, 'core/singup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/contact/')  # Redirect to home page after successful login
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})