from django import forms
from django.contrib.auth.forms import UserCreationForm

from Vapp.models import *


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class NurseRegistration(forms.ModelForm):
    class Meta:
        model = nurse
        fields = ('name', 'address', 'contact_no', 'Email', 'Hospital_name')


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ('Name', 'Address', 'contact_no', 'Child_name', 'child_age', 'child_gender', 'Recent_vaccination')


class hospitalform(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ('name', 'place', 'contact_no', 'Email')


class vaccineform(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ('vaccine_name', 'vaccine_type', 'Description',)


class reportcardform(forms.ModelForm):
    class Meta:
        model = Reportcard
        fields = ('Patient', 'vaccine')


class scheduleform(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('hospital', 'date', 'start_time', 'end_time')


class complaintform(forms.ModelForm):
    class Meta:
        model = Complaint_Details
        fields = ('user','subject', 'complaint', 'date')
