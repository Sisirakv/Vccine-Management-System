from django.contrib import messages
from django.shortcuts import render, redirect
from Vapp.form import *


def Add_Complaints(request):
    form = complaintform()
    if request.method == "POST":
        form = complaintform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully added')
            return redirect('Your_Complaints')
        # else:
        #     form = complaintform(request.POST)
    return render(request, 'UserView_temp/Complaint.html', {'form': form})


def user_profile(request):
    u = request.user
    data = User.objects.filter(user=u)
    return render(request, 'UserView_temp/Profile.html', {'data': data})


def profile_update(request, user_id):
    profile = User.objects.get(user_id=user_id)

    if request.method == 'POST':
        form = UserProfileUpdate(request.POST or None, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile Updated Successfully')
            return redirect('user_profile')
    else:
        form = UserProfileUpdate(instance=profile)

    return render(request, 'UserView_temp/profile_update.html', {'form': form})


def fixschedules(request):
    data = Schedule.objects.all()
    return render(request, 'UserView_temp/FixAppointments.html', {'data': data})


def compaintview(request):
    data = Complaint_Details.objects.all()
    return render(request, 'UserView_temp/viewUser_Complaint.html', {'data': data})


def complaintDelete_User(request, id):
    data = Complaint_Details.objects.get(id=id)
    data.delete()
    return redirect('Your_Complaints')


def complaintUpdate_user(request, id=None):
    n = Complaint_Details.objects.get(id=id)
    if request.method == 'POST':
        form = complaintform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
        return redirect('User_Complaints')
    else:
        form = complaintform(request.POST or None, instance=n)
    return render(request, 'UserView_temp/Complaint.html', {'form': form})


def take_appointment(request, id):
    schedule = Schedule.objects.get(id=id)
    u = User.objects.get(user=request.user)
    appointment = Appointment_Details.objects.filter(user=u, schedule=schedule)
    if appointment.exists():
        messages.info(request, "You have already requested to this Schedule")
        return redirect('Appointment')
    else:
        if request.method == 'POST':
            obj = Appointment_Details()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, "Appointment Booked Successfully")
            return redirect('Appointment')
    return render(request, 'UserView_temp/TakeAppointment.html', {'schedule': schedule})


def appointment(request):
    u = User.objects.get(user=request.user)
    a = Appointment_Details.objects.filter(user=u)
    return render(request, 'UserView_temp/appointments.html', {'appointment': a})



def report(request):
    u = User.objects.get(user=request.user)
    data = Reportcard.objects.filter(Patient=u)
    return render(request, 'UserView_temp/ReportCard.html', {'data': data})
