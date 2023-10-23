from django.shortcuts import render,redirect
from student.models import *

def home(request):
          return render(request,"student/home.html",{})

def std_add(request):
        if request.method == "POST":
                print("added")
                #retrieve user input
                stds_roll = request.POST.get("std_roll")
                print(stds_roll)          
                stds_name = request.POST.get("std_name")  
                print(stds_name)        
                stds_email = request.POST.get("std_email")
                print(stds_email)
                stds_address = request.POST.get("std_address")
                print(stds_address)
                stds_phone = request.POST.get("std_phone")
                print(stds_phone)

                #create an object for models
                s=Student()
                s.roll=stds_roll
                s.name=stds_name
                s.email=stds_email
                s.adddress=stds_address
                s.phone=stds_phone
                s.save()
                return redirect("/student/home")
                 
                
        return render(request,"student/add_std.html",{})