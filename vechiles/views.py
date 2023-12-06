from django.shortcuts import render,redirect
from django.views.generic import FormView,TemplateView,ListView,DetailView,UpdateView
from vechiles.forms import RegistrationForm,LoginForm,VechileCreateForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from vechiles.models import Vechiles
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"please signin first")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

def is_admin(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            messages.error(request,"Permission Denied for Current User")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

desc = [signin_required, is_admin]

class SignupView(FormView):
    template_name="olxapp/signup.html"
    form_class=RegistrationForm

    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull")
            return redirect("signin")
        else:
            messages.error(request,"Registration Failed")
            return render(request,"olxapp/signup.html",{"form":form})
        
class SignInView(FormView):
    template_name="olxapp/signin.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                # messages.success(request,"Loged Succussfully")
                return redirect("list")
            else:
                messages.error(request,"Login Failed")
                return render(request,"olxapp/signin.html",{"form":form})
        else:
            return render(request,"olxapp/signin.html",{"form":form})

@signin_required       
def logoutview(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

@method_decorator(desc, name="dispatch")      
class IndexView(TemplateView):
    template_name="olxapp/index.html"

@method_decorator(desc, name="dispatch")
class VechileCreateView(FormView):
    template_name="olxapp/add.html"
    form_class=VechileCreateForm

    def post(self,request,*args,**kwargs):
        form=VechileCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            Vechiles.objects.create(**form.cleaned_data,user=request.user)
            messages.success(request,"Vechicle Created Successfully")
            return redirect("list")
        else:
            messages.error(request,"Creation Failed")
            return render(request,self.template_name,{"form":form})
        
@method_decorator(desc, name="dispatch")
class VechileListView(ListView):
    template_name = "olxapp/list.html"
    context_object_name = "list"
    model = Vechiles 

@method_decorator(desc, name="dispatch")
class VechileDetailView(DetailView):
    template_name = "olxapp/detail.html"
    context_object_name = "detail"
    model = Vechiles

@signin_required
@is_admin
def delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    Vechiles.objects.filter(id=id).delete()
    return redirect("list")

@method_decorator(desc, name="dispatch")
class VechileUpdateView(UpdateView):
    template_name = "olxapp/update.html"
    form_class = VechileCreateForm
    model = Vechiles
    success_url = reverse_lazy("list")

