from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from .models import *

# Create your views here.

def index(request):
    

    return render (request,'vehcare.html')

def customersignup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cnfpassword=request.POST['cnfpassword']

        if password==cnfpassword:
            if User.objects.filter(username=username):
                print('Username already exists')
                return redirect('/custsignup')
            elif User.objects.filter(email=email):
                print("email already exist")
                return redirect('/custsignup')
            else :
                User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                print('New user created successfully')
                return redirect('/')
        else:
            print("password does not matched") 
            return redirect('/custsignup')
    else:
        return render(request,'usersignup.html') 

def customersignin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print('user login successfully')
            return redirect('/home')
        else:
            print('invalid creditials')
            return redirect('/')
    else:

        return render(request,'usersignin.html')  

def logout_user(request):
    auth.logout(request)
    return redirect('/')

def customerprofile(request):
    if request.method=="POST":
        print('inside post')
        user=request.user
        userobj=User.objects.get(id=user.id)
        print(userobj)
        mobnumber=request.POST.get('mobnumber')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        state=request.POST.get('state')
        city=request.POST.get('city')
        
        vehicalno=request.POST.get('vehnumber')

        try:
            profpic=request.FILES.get('profimage')
        except:
            profpic=None 

        # if MechanicProfile.objects.get(user=userobj):
        #     print('profile for mechanic is already created')    
        #     return redirect('/index') 
        # else:    
        CustomerProfile.objects.create(user=userobj,mobnumber=mobnumber,dob=dob,address=address,state=state,city=city,profpic=profpic,vehicalno=vehicalno)
        print('customer profile created successfully')
        return redirect('/home')
    else:           
        return render (request,'profile.html')

def mechanicprofile(request):
    if request.method=="POST":
        print('inside mechanic profile')
        user=request.user
        mecanicobj=User.objects.get(id=user.id)
        mobnumber=request.POST.get('mobnumber')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        state=request.POST.get('state')
        city=request.POST.get('city')
        
        vehicalno=request.POST.get('vehnumber')

        try:
            profpic=request.FILES.get('profimage')
        except:
            profpic=None

        # if MechanicProfile.objects.get(user=mecanicobj) :
        #     print('Mechanic profile is already created')
        #     return redirect('/index')
        # else:

        MechanicProfile.objects.create(user=mecanicobj,mobnumber=mobnumber,dob=dob,address=address,state=state,city=city,profpic=profpic,vehicalno=vehicalno) 
        print('mechanic profile creatted successfully') 
        return redirect('/homemechanic') 
           
    else:
        return render (request,'profile_mechanic.html')   

def home(request):
    user=request.user
   
    if CustomerProfile.objects.filter(user=user):
        custobj=CustomerProfile.objects.get(user=user)
        
    else:
        
        custobj=None

    if MechanicProfile.objects.filter(user=user):
        mechobj=MechanicProfile.objects.get(user=user) 
    else:
        mechobj=None       

    context={'custobj':custobj,'mechobj':mechobj}  
    print('shilpa',context)
    
    return render(request,'home.html',context)  

def viewprofile_mechanic(request):
    user=request.user
    if MechanicProfile.objects.filter(user=user):
        mechprofobj=MechanicProfile.objects.get(user=user)
        print('mechprofobj',mechprofobj)
    else:
        mechprofobj=None    

    context={'mechprofile':mechprofobj}
    print('mechprofobj',context)
    return render (request,'profmech_view.html',context)         
    
def home_mechanic(request):
    user=request.user
    if MechanicProfile.objects.filter(user=user):
        mechprofobj=MechanicProfile.objects.get(user=user)
        print('mechprofobj',mechprofobj)
    else:
        mechprofobj=None    

    context={'mechprofile':mechprofobj}
    print('mechprofobj',context)
    return render(request,'home_mechanic.html',context)                
