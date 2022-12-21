from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerProfile(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    mobnumber=models.IntegerField()
    dob=models.DateField(null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    state=models.CharField(max_length=30,null=True,blank=True)
    city=models.CharField(max_length=30,null=True,blank=True)
    profpic=models.ImageField(upload_to='images',default='')
    vehicalno=models.IntegerField()

class MechanicProfile(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    mobnumber=models.IntegerField()
    dob=models.DateField(null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    state=models.CharField(max_length=30,null=True,blank=True)
    city=models.CharField(max_length=30,null=True,blank=True)
    profpic=models.ImageField(upload_to='images',default='')
    vehicalno=models.IntegerField()    



