from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Category,Product
# Create your views here.

def index(request):
    return render(request,"admin_index.html")

def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        if uname=='admin' and upass=='12345':
            return redirect('/dashboard/')
        else:
            return HttpResponse("Invalid username or Password!!!")
    return render(request,"admin_login.html")


def dashboard_view(request):
    return render(request,"dashboard.html")

def addproduct_view(request):
    
    cats = Category.objects.all()
    if request.method == 'POST':
        n = request.POST.get('name')
        p = request.POST.get('price')
        c=request.POST.get('category')
        d = request.POST.get('des')
        i = request.FILES['image']
        print(n, p,  d, i)
        
        # # Fetch the category instance
        category_instance = Category.objects.get(id=c)
        
        # Create and save the product
        
        obj = Product(name=n, price=p, des=d, image=i,category=category_instance )
        obj.save()
        return redirect('/viewproduct/')
    return render(request,"addproduct.html",{'cats':cats})

def viewproduct_view(request):
    prods=Product.objects.all()
    return render(request,'viewproduct.html',{'prods':prods})
def edit(req):
    return HttpResponse("edit")

def delite(req):
    return HttpResponse("delite")


def addcat(request):
    
    
    if request.method == 'POST':
        n = request.POST.get('name')
        d = request.POST.get('des')
        
        obj = Category(name=n,des=d)
        obj.save()
        # return redirect('/viewproduct/')
    return render(request,"addcat.html")