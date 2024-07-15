from django.shortcuts import render,redirect,get_object_or_404
import os
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from app.models import Category,Product,Productcard

from django.contrib.auth import login
def fun1(req):
    return render(req,'base.html')
def fun2(req):
    catppp=Category.objects.all()
    return render(req,'cats.html',{'catppp':catppp})

def fun3(request):
    

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/cats/')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    return render(request,'login.html')



def Categoryp(request):
    
    
    if request.method == 'POST':
        n = request.POST.get('name')
        d = request.POST.get('des')
        
        obj = Category(name=n,des=d)
        obj.save()

        return redirect('/cats/')
    return render(request,"addcats.html")

def Product1(request):
    
    if request.method == 'POST':
        n = request.POST.get('name')
        d = request.POST.get('des')
        i=request.FILES['image']
        
        obj = Product(name=n,des=d,img=i)
        obj.save()

        return redirect('/datadisp/')
    return render(request,"addprod.html")

def datadisp(req):
    catppp=Category.objects.all()
    prod=Product.objects.all()
    return render(req,'datadisp.html',{'catppp':catppp,'prod':prod})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        
        if 'image' in request.FILES:
            if product.img:
                # Delete the old image file from the filesystem
                if os.path.isfile(product.img.path):
                    os.remove(product.img.path)
            # Update the product's image with the new one
            product.img = request.FILES['image']
        
        product.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('/datadisp/')
    
    return render(request, 'editproduct.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('/datadisp/')
    return render(request, 'deleteproduct.html', {'product': product})


def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        
        if 'image' in request.FILES:
            if product.img:
                # Delete the old image file from the filesystem
                if os.path.isfile(product.img.path):
                    os.remove(product.img.path)
            # Update the product's image with the new one
            product.img = request.FILES['image']
        
        product.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('/datadisp/')
    
    return render(request, 'editproduct.html', {'product': product})


    
def buyproduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']

        if 'image' in request.FILES:
            if product.img:
                # Delete the old image file from the filesystem
                if os.path.isfile(product.img.path):
                    os.remove(product.img.path)
            # Update the product's image with the new one
            product.img = request.FILES['image']
        
        product.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('/datadisp/')
    
    return render(request, 'datadisp.html', {'product': product})

def cardprod(req):
    
    catppp=Category.objects.all()
    prod=Productcard.objects.all()
    return render(req,'cardprod.html',{'catppp':catppp,'prod':prod})