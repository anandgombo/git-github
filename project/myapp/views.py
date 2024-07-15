from django.shortcuts import render
from django.http import HttpResponseRedirect
from myapp.models import data
# Create your views here.
def home(req):
    return render(req,'home.html')
def disp(req):
    obj=data.objects.all()
    return render(req,'disp.html',{'obj':obj})
def form(req):
    if req.method == 'POST':
        n=req.POST.get('name')
        r=req.POST.get('roll')
        i=req.FILES['img']
        print(n,r,i)
        obj=data(name=n,roll=r,img=i)
        obj.save()
        # dic={"n":n,'r':r,'i':i}
    return render(req,'form.html')