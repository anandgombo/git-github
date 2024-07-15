from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from main.models import Product
from django.contrib import messages
def index(request):
    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})

def dashboard(request):
    products = Product.objects.all()
    total_products = products.count()
    total_revenue = sum(product.price for product in products)
    total_orders = 0  # This should be updated to reflect actual orders if you have an Order model

    context = {
        'products': products,
        'total_products': total_products,
        'total_revenue': total_revenue,
        'total_orders': total_orders,
    }
    return render(request, 'main/dashboard.html', context)


def master(req):
    return render(req,'main/master.html')

def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        product = Product(name=name, description=description, price=price)
        product.save()
        messages.success(request, 'Product added successfully!')
        return redirect('dashboard')
    return render(request, 'main/addproduct.html')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('home')
    return render(request, 'main/editproduct.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('home')
    return render(request, 'main/deleteproduct.html', {'product': product})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')