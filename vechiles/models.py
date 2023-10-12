from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vechiles(models.Model):
    name=models.CharField(max_length=200)
    mnf_year=models.DateTimeField()
    fuel_option={
        ("petrol","Petrol"),
        ("desel","Desel"),
        ("cng","CNG")
    }
    fuel_type=models.CharField(max_length=200,choices=fuel_option,default="petrol")
    rided_km=models.IntegerField()
    gear_option={
        ("manual","Manual"),
        ("automatic","Automatic"),
        ("no_gear","No Gear")
    }
    gear=models.CharField(max_length=500,choices=gear_option,default="manual")
    seat=models.IntegerField()
    price=models.IntegerField(null=True)
    location=models.CharField(max_length=500)
    posting_date=models.DateField(auto_now_add=True,null=True)
    discription=models.CharField(max_length=1000)
    phone=models.CharField(max_length=20,null=True)
    image=models.ImageField(upload_to="images",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name