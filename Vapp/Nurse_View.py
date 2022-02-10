from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from Vapp.form import *


def userdetails(request):
    data = nurse.objects.all()
    return render(request, 'NurseView_temp/viewUser_Nurse.html', {'data': data})

def hospitaldetails(request):
    data = Hospital.objects.all()
    return render(request, 'NurseView_temp/viewHospital_Nurse.html', {'data': data})

def Add_Complaints(request):

    if request.method == "POST":
        form = complaintform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully added')
            return redirect('Nurse_page')
    else:
        form = complaintform()
    return render(request, 'NurseView_temp/Add_Complaint.html', {'form': form})

# def Add_Complaints(request):
#     # u = request.user
#     if request.method == "POST":
#         form = complaintform(request.POST)
#         if form.is_valid():
#             form1 = form.save(commit=False)
#             # form1.user=u
#             form1.save()
#             messages.info(request, 'Successfully added')
#             return redirect('Nurse_page')
#     else:
#         form = complaintform()
#     return render(request, 'NurseView_temp/Add_Complaint.html', {'form': form})

def viewcomplaints (request):
    data=Complaint_Details.objects.all()
    return render (request,'NurseView_temp/Add_Complaints.html',{'data':data})


def Add_Schedule(request):
    form = scheduleform()
    if request.method == "POST":
        form = scheduleform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully added')
            return redirect('Nurse_page')
    return render(request, 'NurseView_temp/Add_Appointment.html', {'form': form})


def viewappointments(request):
    data = Appointment_Details.objects.all()
    return render(request, 'AdminView_temp/viewAppointments.html', {'data': data})

def viewvaccine(request):
    data = Vaccine.objects.all()
    return render(request, 'AdminView_temp/viewVaccine.html', {'data': data})