from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from Vapp.form import *

from Vapp.filter import VaccineFilter, ScheduleFilter, UserFilter, HospitalFilter


# def userdetails(request):
#     data = User.objects.all()
#     return render(request, 'NurseView_temp/viewUser_Nurse.html', {'data': data})


def userdetails(request):
    v = User.objects.all()
    userFilter = UserFilter(request.GET, queryset=v)
    v = userFilter.qs
    context = {
        'user': v,
        'userFilter': userFilter,
    }
    return render(request, 'NurseView_temp/viewUser_Nurse.html', context)


# def hospitaldetails(request):
#     data = Hospital.objects.all()
#     return render(request, 'NurseView_temp/viewHospital_Nurse.html', {'data': data})


def hospitaldetails(request):
    v = Hospital.objects.all()
    hospitalFilter = HospitalFilter(request.GET, queryset=v)
    v = hospitalFilter.qs
    context = {
        'hospital': v,
        'hospitalFilter': hospitalFilter,
    }
    return render(request, 'NurseView_temp/viewHospital_Nurse.html', context)


def Add_Complaints(request):
    form = complaintform()
    if request.method == "POST":
        form = complaintform(request.POST)
        if form.is_valid():
            form.save()
            print('hi')
            messages.info(request, 'Successfully added')
            return redirect('Complaint_Details')
    # else:
    #     form = complaintform()
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

def viewcomplaints(request):
    data = Complaint_Details.objects.all()
    return render(request, 'NurseView_temp/Add_Complaints.html', {'data': data})


def Add_Schedule(request):
    form = scheduleform()
    if request.method == "POST":
        form = scheduleform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully added')
            return redirect('Schedule_Details')
    return render(request, 'NurseView_temp/Add_Appointment.html', {'form': form})


def appointmentdetails(request):
    data = Appointment_Details.objects.all()
    return render(request, 'NurseView_temp/viewAppointments_Nurse.html', {'data': data})


# def vaccinedetails(request):
#     data = Vaccine.objects.all()
#     return render(request, 'NurseView_temp/viewVaccine_Nurse.html', {'data': data})


def vaccinedetails(request):
    v = Vaccine.objects.all()
    vaccineFilter = VaccineFilter(request.GET, queryset=v)
    v = vaccineFilter.qs
    context = {
        'vaccine': v,
        'vaccineFilter': vaccineFilter,
    }
    return render(request, 'NurseView_temp/viewVaccine_Nurse.html', context)


# def viewschedules(request):
#     data = Schedule.objects.all()
#     return render(request, 'NurseView_temp/viewShecdules_Nurse.html', {'data': data})


def viewschedules(request):
    v = Schedule.objects.all()
    scheduleFilter = ScheduleFilter(request.GET, queryset=v)
    v = scheduleFilter.qs
    context = {
        'Schedule': v,
        'scheduleFilter': scheduleFilter,
    }
    return render(request, 'NurseView_temp/viewShecdules_Nurse.html', context)


def viewcomplaints_nurse(request):
    data = Complaint_Details.objects.all()
    return render(request, 'NurseView_temp/viewNurse_Complaint.html', {'data': data})


def appointmentDelete(request, id=None):
    data = Schedule.objects.get(id=id)
    data.delete()
    return redirect('Schedule_Details')


def scheduleUpdate(request, id=None):
    n = Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = scheduleform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
        return redirect('Schedule_Details')
    else:
        form = scheduleform(request.POST or None, instance=n)
    return render(request, 'NurseView_temp/Add_Appointment.html', {'form': form})


def complaintDelete(request, id=None):
    data = Complaint_Details.objects.get(id=id)
    data.delete()
    return redirect('Complaint_Details')


def complaintUpdate(request, id=None):
    n = Complaint_Details.objects.get(id=id)
    if request.method == 'POST':
        form = complaintform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
        return redirect('Complaint_Details')
    else:
        form = complaintform(request.POST or None, instance=n)
    return render(request, 'NurseView_temp/Add_Complaint.html', {'form': form})


def Add_Reportcard(request):
    form = reportcardform()
    if request.method == "POST":
        form = reportcardform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Reportcard Successfully added')
            return redirect('View_ReportCard')
    return render(request, 'NurseView_temp/Add_ReportCard.html', {'form': form})


def viewcard(request):
    data = Reportcard.objects.all()
    return render(request, 'NurseView_temp/viewReportCard.html', {'data': data})


def reportcardDelete(request, id=None):
    data = Reportcard.objects.get(id=id)
    data.delete()
    return redirect('View_ReportCard')


def reportcardUpdate(request, id=None):
    n = Reportcard.objects.get(id=id)
    if request.method == 'POST':
        form = reportcardform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
        return redirect('viewReportCard')
    else:
        form = reportcardform(request.POST or None, instance=n)
    return render(request, 'NurseView_temp/Add_ReportCard.html', {'form': form})


def mark_vaccinated(request, id):
    a = Appointment_Details.objects.get(id=id)
    vaccine = Vaccine.objects.filter(approval_status=0)
    context = {
        'vaccine': vaccine,
        'a': a,
    }
    try:
        if request.method == 'POST':
            vacc = request.POST.get('vaccine')
            a.vaccinated = True
            a.vaccine_name = Vaccine.objects.get(id=vacc)
            a.save()
            return redirect('Schedule_Details')
    except ValueError:
        messages.info(request, 'Please Select a Vaccine')
    return render(request, 'NurseView_temp/mark_vaccinated.html', context)



