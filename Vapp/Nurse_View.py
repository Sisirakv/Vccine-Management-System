from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from Vapp.form import *


def userdetails(request):
    data = User.objects.all()
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


def appointmentdetails(request):
    data = Appointment_Details.objects.all()
    return render(request, 'NurseView_temp/viewAppointments_Nurse.html', {'data': data})

def vaccinedetails(request):
    data = Vaccine.objects.all()
    return render(request, 'NurseView_temp/viewVaccine_Nurse.html', {'data': data})

def viewschedules(request):
    data = Schedule.objects.all()
    return render(request, 'NurseView_temp/viewShecdules_Nurse.html', {'data': data})

def viewcomplaints_nurse(request):
    data = Complaint_Details.objects.all()
    return render(request, 'NurseView_temp/viewNurse_Complaint.html', {'data': data})

def appointmentDelete(request,id=None):
    data = Schedule.objects.get(id=id)
    data.delete()
    return redirect ('Schedule_Details')

def scheduleUpdate(request, id=None):
    updt_data = Schedule.objects.get(id=id)
    if request.method == 'POST':
        hospital = request.POST['hospital']
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        updt_data.hospital = hospital
        updt_data.date = date
        updt_data.start_time = start_time
        updt_data.end_time = end_time
        updt_data.save()
        return redirect('Schedule_Details')
    return render(request, 'NurseView_temp/Add_Appointment.html', {'updt_data': updt_data})

def complaintDelete(request,id=None):
    data = Complaint_Details.objects.get(id=id)
    data.delete()
    return redirect ('Complaint_Details')

def complaintUpdate(request, id=None):
    updt_data = Complaint_Details.objects.get(id=id)
    if request.method == 'POST':

        subject = request.POST['subject']
        complaint = request.POST['complaint']
        date = request.POST['date']

        updt_data.subject = subject
        updt_data.complaint = complaint
        updt_data.date = date
        updt_data.save()
        return redirect('Complaint_Details')
    return render(request, 'NurseView_temp/Add_Complaint.html', {'updt_data': updt_data})