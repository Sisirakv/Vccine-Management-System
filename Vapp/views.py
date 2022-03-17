from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from Vapp.form import *


# Create your views here.


def ind(request):
    return render(request, 'Admin_Home.html')


def Home(request):
    return render(request, 'Home_pagemain.html')


def login(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            if user.is_staff:
                return redirect('admin_page')
            elif user.is_nurse:
                return redirect('Nurse_page')
            elif user.is_user:
                return redirect('User_page')

        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')


def nurseHome(request):
    return render(request, 'Nurse_Home.html')


def userHome(request):
    return render(request, 'User_Home.html')


def nurse_register(request):
    login_form = LoginRegister()
    nurse_form = NurseRegistration()
    if request.method == "POST":
        login_form = LoginRegister(request.POST)
        nurse_form = NurseRegistration(request.POST)
        if login_form.is_valid() and nurse_form.is_valid():
            user = login_form.save(commit=False)
            user.is_nurse = True
            user.save()
            nurse = nurse_form.save(commit=False)
            nurse.user = user
            nurse.save()
            messages.info(request, 'Nurse Registration Successfully')
            return redirect('login')
    return render(request, 'NurseRegister.html', {'login_form': login_form, 'nurse_form': nurse_form})


def user_register(request):
    login_form = LoginRegister()
    user_form = UserRegistration()
    if request.method == "POST":
        login_form = LoginRegister(request.POST)
        user_form = UserRegistration(request.POST)
        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            c = user_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, 'User Registration Successfully')
            return redirect('login')
    return render(request, 'UserRegister.html', {'login_form': login_form, 'user_form': user_form})
