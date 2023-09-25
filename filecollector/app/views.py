from django.shortcuts import render
from . import forms
from .models import User,files
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request , "index.html")
def register(request):
    form=forms.Register()
    if request.method=="POST":
        formdata=forms.Register(request.POST)
        msg = "failed"
        if formdata.is_valid():
            formdata.save()
            msg="register successfully"
        return render(request,"register.html",{"userform":form,"msg":msg})
    return render(request, "register.html", {"userform": form})


def login(request):
    return render(request,"login.html")
def checklogin(request):
    if request.method=="POST":
        emailid=request.POST['email']
        password=request.POST['password']
        exist=User.objects.filter(Q(email=emailid) and Q(password=password))
        if exist:
            user=User.objects.get(email=emailid)
            request.session["id"]=user.id
            request.session.set_expiry(6000)

            msg=request.session["id"]
            return render(request,"addproduct.html",{"msg":msg})
        else:
            return render(request, "login.html")

    return render(request, "login.html")
def userhome(request):
    id = request.session.setdefault('id', 0)
    print(id)
    i=request.session["id"]
    if id==0:
        return render(request, "index.html")
    else:
        return render(request,"userhome.html" ,{"id":id})
def addproduct(request):
    form = forms.upload()
    id = request.session.setdefault('id', 0)
    if id!=0:
        if request.method == "POST" :
            id = request.session["id"]
            file=request.FILES["file"]
            w=files(id=id,file=file)
            files.save(w)
            msg="added"
            return render(request, "addproduct.html", { "msg": msg})
            formdata = forms.upload(request.POST,request.FILES)
            """if formdata.is_valid():
                formdata.save()
                msg="Product Added Successfully"
                return render(request, "addproduct.html", {"auname":id,"productform": form,"msg":msg})
            else:
                msg = "Failed to Add Product"
                return render(request, "addproduct.html", {"auname":id,"productform": form, "msg": msg})"""
        else:
            # msg = "Failed to Add Product"
            return render(request, "index.html")
    return render(request,"addproduct.html")


def rigi(request):
    if request.method=="POST":
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        u=User(email=email,username=username,password=password)
        u.save()
        msg="registered"
        return render(request,"register.html",{"msg":msg})
    return render(request,"register.html")
def logout(request):
    request.session["id"]=0
    return render(request,"index.html")

