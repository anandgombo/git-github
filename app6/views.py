from django.shortcuts import render
from app6.models import singup
 
# Create your views here.
dict_data={}
def data(req):    
    dict_data=singup.objects.all()    
    return render(req,'data.html',{'dict_data':dict_data})


def login(req):
    global dict_data
    try:
        if req.method=='post':
          ps=req.post.get('password')
          e=req.post.get('email')
          dict_data['password']=ps
          dict_data['email']=e
    except:
        pass
    return render(req,'login.html',dict_data)

def sing_form(req):
        n=0
        e=0
        p=0
        ps=0
        cps=0
       
        if req.method=='POST':
            n=req.POST.get('name')
            e=req.POST.get('email')
            p=req.POST.get('phone')
            ps=req.POST.get('password')
            cps=req.POST.get('compass')
        obj=singup(name=n,email=e,phone=p,password=ps,compass=cps)
        obj.save()
        print("============================",n,e,p,ps,cps)

        return render(req,"form.html")

def home(req):
    return render(req,'master.html')
