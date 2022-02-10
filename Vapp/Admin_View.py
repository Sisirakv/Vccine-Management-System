from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from Vapp.form import *


def Add_Hospitals(request):
    form = hospitalform()
    if request.method == "POST":
        form = hospitalform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully added')
            return redirect('admin_page')
    return render(request, 'AdminView_temp/Add_Hospitals.html', {'form': form})


def viewnurse(request):
    data = nurse.objects.all()
    return render(request, 'AdminView_temp/viewNurse.html', {'data': data})


def viewuser(request):
    data = User.objects.all()
    return render(request, 'AdminView_temp/viewUser.html', {'data': data})


def viewhospital(request):
    data = Hospital.objects.all()
    return render(request, 'AdminView_temp/viewHospital.html', {'data': data})


def Add_Vaccine(request):
    form = vaccineform()
    if request.method == "POST":
        form = vaccineform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Vaccine Successfully added')
            return redirect('admin_page')
    return render(request, 'AdminView_temp/Add_Vaccine.html', {'form': form})


def viewvaccine(request):
    data = Vaccine.objects.all()
    return render(request, 'AdminView_temp/viewVaccine.html', {'data': data})


def Add_Reportcard(request):
    form = reportcardform()
    if request.method == "POST":
        form = reportcardform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Reportcard Successfully added')
            return redirect('admin_page')
    return render(request, 'AdminView_temp/Add_ReportCard.html', {'form': form})


def viewcard(request):
    data = Reportcard.objects.all()
    return render(request, 'AdminView_temp/viewReportCard.html', {'data': data})


def viewappointments(request):
    data = Appointment_Details.objects.all()
    return render(request, 'AdminView_temp/viewAppointments.html', {'data': data})


def viewcomplaints(request):
    data = Complaint_Details.objects.all()
    return render(request, 'AdminView_temp/viewComplaints.html', {'data': data})
