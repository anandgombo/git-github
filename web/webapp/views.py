from django.shortcuts import render,redirect
from django.contrib import messages

from django.http import HttpResponse
from webapp.models import Item
# Create your views here.
def index(req):
    return render(req,'index.html')

def add(req):
    return render(req,'add.html')

def addProduct(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')

        if len(request.FILES) != 0:
            image = request.FILES['image']

        obj=Item(name=name,description=description,price=price,image=image)
        obj.save()
        messages.success(request, "Product Added Successfully")
        return redirect('/')
    return render(request, 'add.html')

def show(req):
    obj=Item.objects.all()

    return render(req,'show.html',{'obj':obj})

# from django.shortcuts import render
# from .models import Item  # Import your Item model here

# def delete(req):
#     if req.method == 'POST':
#         id = req.POST.get('input')
#         print("Received ID:", id)
#         # Perform deletion logic here
#         try:
#             item_to_delete = Item.objects.get(id=id)
#             item_to_delete.delete()
#             print("Item deleted successfully!")
#             # Redirect or return a success response
#         except Item.DoesNotExist:
#             print("Item with ID {} does not exist.".format(id))
#             # Handle the case where the item does not exist
#             # Redirect or return an error response
#     return render(req, 'del.html')

def delete(req):
    if req.method == 'POST':
        id = req.POST.get('input')
        print("Received ID:", id)
        try:
            item_to_delete = Item.objects.get(id=id)
            print("Item deleted successfully!")
            item_to_delete.delete()
        except Item.DoesNotExist:
            print("Item with ID {} does not exist.".format(id))
    return render(req, 'del.html')

def edit(req):
    item = Item.objects.all()
    return render(req, 'edit.html', {'obj': item})
    # try:
    #     item = Item.objects.get(pk=req.GET.get('id'))  # Assuming 'id' is passed as a parameter
    #     return render(req, 'edit.html', {'obj': item})
    # except Item.DoesNotExist:
    #     # Handle the case where the item does not exist
    #     return HttpResponse("Item does not exist.")
