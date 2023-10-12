from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from vechiles.models import Vechiles

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        labels={
            "first_name":"FIRST NAME",
            "last_name":"LAST NAME",
            "email":"EMAIL ID",
            "username":"USERNAME"
        }
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter First Name','style':'width:80%;'}),
            "last_name":forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Last Name','style':'width:80%;'}),
            "email":forms.EmailInput(attrs={"class":"form-control",'placeholder':'Enter Email','style':'width:80%;'}),
            "username":forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Username','style':'width:80%;'})
        }

class LoginForm(forms.Form):
    username=forms.CharField(label="USERNAME",widget=forms.TextInput(attrs={"class":"form-control","style":"width:80%;",
                                                                            "placeholder":"Enter Username"}))
    password=forms.CharField(label="PASSWORD",widget=forms.PasswordInput(attrs={"class":"form-control","style":"width:80%;",
                                                                                "placeholder":"Enter Password"}))
    
class VechileCreateForm(forms.ModelForm):
    class Meta:
        model=Vechiles
        fields=["name","mnf_year","fuel_type","rided_km","gear","seat","price","location","discription","phone","image"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Name of Vechile','style':'width:80%;'}),
            "mnf_year":forms.DateInput(attrs={"class":"form-control","type":"date",'style':'width:80%;'}),
            "fuel_type":forms.Select(attrs={"class":"form-select",'style':'width:80%;'}),
            "rided_km":forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter KM','style':'width:80%;'}),
            "gear":forms.Select(attrs={"class":"form-select",'style':'width:80%;'}),
            "seat":forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter No. of Seats','style':'width:80%;'}),
            "price":forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Price','style':'width:80%;'}),
            "location":forms.Textarea(attrs={"class":"form-control",'placeholder':'Enter Address','style':'width:80%;'}),
            "discription":forms.Textarea(attrs={"class":"form-control",'placeholder':'Write any discription','style':'width:80%;'}),
            "phone":forms.TextInput(attrs={"class":"form-control",'placeholder':'Enter Your Mobile number','style':'width:80%;'})
        }