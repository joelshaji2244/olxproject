from django import forms
from olx.models import Olx
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class OlxCreateForm(forms.ModelForm):
    class Meta:
        model=Olx
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "mnf_year":forms.TextInput(attrs={"class":"form-control"}),
            "fuel_type":forms.Select(attrs={"class":"form-select"}),
            "rided_km":forms.TextInput(attrs={"class":"form-control"}),
            "gear":forms.Select(attrs={"class":"form-select"}),
            "seat":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.Textarea(attrs={"class":"form-control"}),
            "discription":forms.Textarea(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"})
        }
        labels={
            "name":"Name",
            "mnf_year":"Manufacture Year",
            "fuel_type":"Fuel Type",
            "rided_km":"Rided Kilometer",
            "gear":"Gear Type",
            "seat":"Seat Capacity",
            "price":"Price",
            "location":"Location",
            "discription":"Discription",
            "phone":"Phone Number"
        }