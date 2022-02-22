from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Vapp.form import *


def Add_Complaints(request):
    form = complaintform()
    if request.method == "POST":
        form = complaintform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully added')
            return redirect('User_page')
        else:
            form = complaintform(request.POST)
    return render(request, 'UserView_temp/Complaint.html', {'form': form})


def user_profile(request):
    # data = User.objects.filter(user=request.user)
    # if request.user.is_active:
    data = User.objects.filter()
    return render(request, 'UserView_temp/Profile.html', {'data': data})


# def user_profile(request):
#     data = Hospital.objects.all()
#     return render(request, 'UserView_temp/users-profile.html', {'data': data})

# @login_required(login_url='login')
# def profile_update(request,user_id):
#     profile = User.objects.get(user_id=user_id)
#     if request.method == 'POST':
#         form = UserProfileUpdate(request.POST or None, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.info(request,'Profile Updated Sucessfully')
#             return redirect('user_profile')
#     else:
#         form = UserProfileUpdate(instance=profile)
#
#     return render(request,)

def fixschedules(request):
    data = Schedule.objects.all()
    return render(request, 'UserView_temp/FixAppointments.html', {'data': data})


def compaintview(request):
    data = Complaint_Details.objects.all()
    return render(request, 'UserView_temp/viewUser_Complaint.html', {'data': data})


def complaintDelete_User(request, id=None):
    data = Complaint_Details.objects.get(id=id)
    data.delete()
    return redirect('Your_Complaints')


def complaintUpdate_user(request, id=None):
    n = Complaint_Details.objects.get(id=id)
    if request.method == 'POST':
        form = complaintform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
        return redirect('Complaint_Details')
    else:
        form = complaintform(request.POST or None, instance=n)
    return render(request, 'UserView_temp/Complaint.html', {'form': form})


def take_appointment(request):
    schedule = Schedule.objects.get(schedule=request.schedule)
    u = User.objects.get(user=request.user)
    appointment = Appointment_Details.objects.filter(user=u, schedule=schedule)
    if appointment.exist():
        messages.info(request, "You have already requested to this Schedule")
        return redirect('Schedule_Details')
    else:
        if request.method == 'POST':
            obj = appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, "Appointment Booked Successfully")
            return redirect('Appointments_Details')
    return render(request, 'UserView_temp/TakeAppointment.html', {'schedule': schedule})


def report(request):
    data = Reportcard.objects.all()
    return render(request, 'UserView_temp/ReportCard.html', {'data': data})
