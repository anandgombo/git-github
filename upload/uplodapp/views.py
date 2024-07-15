from django.shortcuts import render

from uplodapp.models import img
# Create your views here.
def home(req):    
    return render(req,'home.html')

def form(req):
    # obj=img.objects.all()
    if req.method == 'POST':
        n=req.POST.get('name')
        s=req.POST.get('sal')
        d=req.POST.get('date')
        p=req.FILES['img']
        print(n,s,d,p)
        obj=img(name=n,date=d,sal=s,photo=p)
        obj.save()
    return render(req,'form.html')

def disp(req):
    obj=img.objects.all()
    return render(req,'disp.html',{'obj':obj})