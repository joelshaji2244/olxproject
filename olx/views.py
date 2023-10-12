from django.shortcuts import render,redirect
from django.views.generic import View
from olx.models import Olx
from olx.forms import OlxCreateForm,RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("olx-login")
        else:
            return render(request,"reg.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                print("creditials are valid")
                login(request,usr)
                return redirect("olx-list")
            else:
                return render(request,"login.html",{"form":form})
        else:
                return render(request,"login.html",{"form":form})    

def logout_view(request,*args,**kwargs):
    logout(request)
    return redirect("olx-login")

class OlxCreateView(View):
    def get(self,request,*args,**kwargs):
        form=OlxCreateForm()
        return render(request,"olx_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=OlxCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("olx-list")
        else:
            return render(request,"olx_add.html",{"form":form})
        
class OlxListView(View):
    def get(self,request,*args,**kwargs):
        qs=Olx.objects.all()
        return render(request,"olx_list.html",{"list":qs})
    
class OlxDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Olx.objects.get(id=id)
        return render(request,"olx_detail.html",{"detail":qs})
    
class OlxDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Olx.objects.filter(id=id).delete()
        return redirect("olx-list")
    
class OlxUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Olx.objects.get(id=id)
        form=OlxCreateForm(instance=obj)
        return render(request,"olx_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Olx.objects.get(id=id)
        form=OlxCreateForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("olx-list")
        else:
            return render(request,"olx_edit.html",{"form":form})