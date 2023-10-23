from django.shortcuts import render,redirect
from student.models import *

def home(request):
          std=Student.objects.all()   #it fetch all the data of student table
          return render(request,"student/home.html",{'std':std})

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
                s.address=stds_address
                s.phone=stds_phone
                s.save()
                return redirect("/student/home")
                 
                
        return render(request,"student/add_std.html",{})


def delete_std(request,roll):
        s=Student.objects.get(pk=roll)
        s.delete()

        return redirect("/student/home")


def update_std(request,roll):
        std=Student.objects.get(pk=roll)
        return render(request,"student/update_std.html",{'std':std})

def do_update_std(request,roll):
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_address=request.POST.get("std_address")
        std_phone=request.POST.get("std_phone")

        std=Student.objects.get(pk=roll)
        std.roll=std_roll
        std.name=std_name
        std.email=std_email
        std.address=std_address
        print(std.address)
        std.phone=std_phone

        std.save()
        return redirect("/student/home")

