from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from Vapp.filters import OrderFilter
from Vapp.filter import *
from Vapp.form import *


# @login_required(login_url='login')
def Add_Hospitals(request):
    form = hospitalform()
    if request.method == "POST":
        form = hospitalform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully added')
            return redirect('admin_page')
    return render(request, 'AdminView_temp/Add_Hospitals.html', {'form': form})


# @login_required(login_url='login')
def viewnurse(request):
    v = nurse.objects.all()
    nurseFilter = NurseFilter(request.GET, queryset=v)
    v = nurseFilter.qs
    context = {
        'user': v,
        'nurseFilter': nurseFilter,
    }
    return render(request, 'AdminView_temp/viewNurse.html', context)


# @login_required(login_url='login')
def viewuser(request):
    v = User.objects.all()
    userFilter = UserFilter(request.GET, queryset=v)
    v = userFilter.qs
    context = {
        'user': v,
        'userFilter': userFilter,
    }
    return render(request, 'AdminView_temp/viewUser.html', context)


# @login_required(login_url='login')
def viewhospital(request):
    v = Hospital.objects.all()
    hospitalFilter = HospitalFilter(request.GET, queryset=v)
    v = hospitalFilter.qs
    context = {
        'hospital': v,
        'hospitalFilter': hospitalFilter,
    }
    return render(request, 'AdminView_temp/viewHospital.html', context)


# @login_required(login_url='login')
def Add_Vaccine(request):
    form = vaccineform()
    if request.method == "POST":
        form = vaccineform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Vaccine Successfully added')
            return redirect('admin_page')
    return render(request, 'AdminView_temp/Add_Vaccine.html', {'form': form})


# @login_required(login_url='login')
def viewvaccine(request):
    v = Vaccine.objects.all()
    vaccineFilter = VaccineFilter(request.GET, queryset=v)
    v = vaccineFilter.qs
    context = {
        'vaccine': v,
        'vaccineFilter': vaccineFilter,
    }
    return render(request, 'AdminView_temp/viewVaccine.html', context)


# @login_required(login_url='login')
def viewappointments(request):
    v = Appointment_Details.objects.all()
    placeFilter = PlaceFilter(request.GET, queryset=v)
    v = placeFilter.qs
    context = {
        'user': v,
        'placeFilter': placeFilter,
    }
    return render(request, 'AdminView_temp/viewAppointments.html', context)


# @login_required(login_url='login')
def appointments(request):
    data = Appointment_Details.objects.all()
    return render(request, 'AdminView_temp/ApprovingAppointment.html', {'data': data})


# @login_required(login_url='login')
def viewcomplaints(request):
    data = Complaint_Details.objects.all()
    return render(request, 'AdminView_temp/viewComplaints.html', {'data': data})


# @login_required(login_url='login')
def hospitalDelete(request, id=None):
    data = Hospital.objects.get(id=id)
    data.delete()
    return redirect('View_Hospital')


# @login_required(login_url='login')
def hospitalUpdate(request, id=None):
    n = Hospital.objects.get(id=id)
    if request.method == 'POST':
        form = hospitalform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
        return redirect('View_Hospital')
    else:
        form = hospitalform(request.POST or None, instance=n)
    return render(request, 'AdminView_temp/Add_Hospitals.html', {'form': form})


# @login_required(login_url='login')
def vaccineDelete(request, id=None):
    data = Vaccine.objects.get(id=id)
    data.delete()
    return redirect('View_Vaccine')


# @login_required(login_url='login')
def vaccineUpdate(request, id=None):
    n = Vaccine.objects.get(id=id)
    if request.method == 'POST':
        form = vaccineform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
        return redirect('View_Vaccine')
    else:
        form = vaccineform(request.POST or None, instance=n)
    return render(request, 'AdminView_temp/Add_Vaccine.html', {'form': form})


# @login_required(login_url='login')
def reply_complaint(request, id):
    complaint = Complaint_Details.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('Reply')
        complaint.reply = r
        complaint.save()
        messages.info(request, 'Reply send for complaints')
        return redirect('View_Complaints')
    return render(request, 'AdminView_temp/Reply.html', {'complaint': complaint})


# @login_required(login_url='login')
def approve_appointment(request, id):
    n = Appointment_Details.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('View_Appointments')


# @login_required(login_url='login')
def reject_appointment(request, id):
    n = Appointment_Details.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('View_Appointments')
