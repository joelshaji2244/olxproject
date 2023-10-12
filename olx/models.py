from django.db import models

# Create your models here.

class Olx(models.Model):
    name=models.CharField(max_length=200)
    mnf_year=models.IntegerField()
    fuel_option={
        ("petrol","Petrol"),
        ("desel","Desel"),
        ("cng","CNG")
    }
    fuel_type=models.CharField(max_length=200,choices=fuel_option,default="petrol")
    rided_km=models.IntegerField()
    options={
        ("manual","Manual"),
        ("automatic","Automatic")
    }
    gear=models.CharField(max_length=500,choices=options,default="manual")
    seat=models.IntegerField()
    price=models.IntegerField(null=True)
    location=models.CharField(max_length=500)
    posting_date=models.DateField(auto_now_add=True,null=True)
    discription=models.CharField(max_length=1000)
    phone=models.CharField(max_length=20,null=True)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.name