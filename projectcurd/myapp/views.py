from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from myapp.models import User
from myapp.forms import form
# Create your views here.
def add_show(req):
    if req.method == 'POST':
        # If a POST request is received, process the form data
        fm = form(req.POST, req.FILES)
        if fm.is_valid():
            # If the form is valid, save the data to the database
            n = fm.cleaned_data['name']
            e = fm.cleaned_data['email']
            p = fm.cleaned_data['password']
            i = fm.files['image']
            obj = User(name=n, email=e, password=p, img=i)
            obj.save()
            # Clear the form after saving the data
            fm = form() 
            # Redirect to the 'show' page after saving the data
            
    else:
        # If a GET request is received, render the form
        fm = form() 
    # Fetch all user objects from the database
    obj = User.objects.all()
    # Render the template with the form and user objects
    return render(req, 'addshow.html', {'fm': fm, 'obj': obj})


def delete(req,id):
    if req.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
 # Import your form class
def update(req, id):
    if req.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = form(req.POST, req.FILES, instance=pi)  # Pass req.FILES for file data and instance for existing object
        if fm.is_valid():
            # Check if there's a new image
            new_image = fm.cleaned_data.get('img')
            if new_image:
                # If a new image is provided, delete the old one
                if pi.img:  # Assuming 'image' is the field for the image upload
                    pi.img.delete()
            fm.save()  # Save the form data including the new image
            return redirect('add_show')  # Redirect after successful form submission
    else:
        pi = User.objects.get(pk=id)
        fm = form(instance=pi)
    return render(req, 'update.html', {'fm': fm})

# def update(req,id):
#     if req.method =='POST':
#         pi=User.objects.get(pk=id)
#         fm=form(req.POST,req.FILES,instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:        
#         pi=User.objects.get(pk=id)
#         fm=form(instance=pi)
#     return render(req,'update.html',{'fm':fm})
    
# def disp(req):
#     obj=data.objects.all()
#     return render(req,'disp.html',{'obj':obj})
# def form(req):
#     if req.method == 'POST':
#         n=req.POST.get('name')
#         r=req.POST.get('roll')
#         i=req.FILES['img']
#         print(n,r,i)
#         obj=data(name=n,roll=r,img=i)
#         obj.save()
#         # dic={"n":n,'r':r,'i':i}
#     return render(req,'form.html')