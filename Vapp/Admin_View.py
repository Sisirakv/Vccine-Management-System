from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from Vapp.form import *


def Add_Hospitals(requset):
    form=hospitalform()
    if requset.method=="POST":
        form=hospitalform(requset.POST)
        if form.is_valid():
            form.save()
            messages.info(requset,'Successfully added')
            return redirect('admin_page')
    return render(requset,'AdminView_temp/Add_Hospitals.html',{'form':form})

def viewnurse (request):
    data=nurse.objects.all()
    return render (request,'AdminView_temp/viewNurse.html',{'data':data})

def viewuser (request):
    data=User.objects.all()
    return render (request,'AdminView_temp/viewUser.html',{'data':data})

def viewhospital (request):
    data=Hospital.objects.all()
    return render (request,'AdminView_temp/viewHospital.html',{'data':data})

def Add_Vaccine(requset):
    form=vaccineform()
    if requset.method=="POST":
        form=vaccineform(requset.POST)
        if form.is_valid():
            form.save()
            messages.info(requset,'Vaccine Successfully added')
            return redirect('admin_page')
    return render(requset,'AdminView_temp/Add_Vaccine.html',{'form':form})

def viewvaccine (request):
    data=Vaccine.objects.all()
    return render (request,'AdminView_temp/viewVaccine.html',{'data':data})