
from django.urls import path
from .import views

urlpatterns = [
    path('index',views.index,name="index"),
    path('custsignup',views.customersignup,name="custsignup"),
    path('',views.customersignin,name="customersignin"),
    path('logout',views.logout_user,name="logout"),
    path('custprofile',views.customerprofile,name="custprofile"),
    path('mechprofile',views.mechanicprofile,name="mechprofile"),
    path('home',views.home,name="home"),
    path('homemechanic',views.home_mechanic,name="homemechanic"),
    path('viewprofilemechanic',views.viewprofile_mechanic,name="viewprofilemechanic"),



]
