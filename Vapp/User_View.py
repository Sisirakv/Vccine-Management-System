from django.contrib import messages
from django.contrib.auth import authenticate
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
    return render(request, 'UserView_temp/complaint.html', {'form': form})


def user_profile(request):
    u = request.user
    profile = User.objects.filter(user=u)
    return render(request, 'UserView_temp/users-profile.html', {'profile': profile})

# def user_profile(request):
#     data = Hospital.objects.all()
#     return render(request, 'UserView_temp/users-profile.html', {'data': data})
