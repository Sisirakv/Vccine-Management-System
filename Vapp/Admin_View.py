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


def reportcardDelete(request, id=None):
    data = Reportcard.objects.get(id=id)
    data.delete()
    return redirect('View_ReportCard')


def reportcardUpdate(request, id=None):
    updt_data = Reportcard.objects.get(id=id)
    if request.method == 'POST':
        Patient = request.POST['Patient']
        vaccine = request.POST['vaccine']
        updt_data.Patient = Patient
        updt_data.vaccine = vaccine
        updt_data.save()
        return redirect('viewReportCard')
    return render(request, 'AdminView_temp/Add_ReportCard.html', {'updt_data': updt_data})

# def reportcardUpdate(request, id=None):
#     updt_data = Reportcard.objects.get(id=id)
#     if request.method == 'POST':
#         updt_data = reportcardform(request.POST)
#         if updt_data.is_valid():
#             updt_data.save()
#         return redirect('viewReportCard')
#     return render(request, 'AdminView_temp/Add_ReportCard.html', {'updt_data': updt_data})

def hospitalDelete(request, id=None):
    data = Hospital.objects.get(id=id)
    data.delete()
    return redirect('View_Hospital')

def hospitalUpdate(request, id=None):
    updt_data = Hospital.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        place = request.POST['place']
        contact_no = request.POST['contact_no']
        Email = request.POST['Email']
        updt_data.name = name
        updt_data.place = place
        updt_data.contact_no = contact_no
        updt_data.Email = Email
        updt_data.save()
        return redirect('View_Hospital')
    return render(request, 'AdminView_temp/Add_Hospitals.html', {'updt_data': updt_data})

def vaccineDelete(request, id=None):
    data = Vaccine.objects.get(id=id)
    data.delete()
    return redirect('View_Vaccine')

def vaccineUpdate(request, id=None):
    updt_data = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        vaccine_name = request.POST['vaccine_name']
        vaccine_type = request.POST['vaccine_type']
        Description = request.POST['Description']
        Approval_status = request.POST['Approval_status']
        updt_data.vaccine_name = vaccine_name
        updt_data.vaccine_type = vaccine_type
        updt_data.Description = Description
        updt_data.Approval_status = Approval_status
        updt_data.save()
        return redirect('View_Vaccine')
    return render(request, 'AdminView_temp/Add_Vaccine.html', {'updt_data': updt_data})