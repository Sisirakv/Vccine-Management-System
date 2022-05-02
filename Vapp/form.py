import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from Vapp.models import *


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


def phone_number_validation(value):
    if not re.compile(r'[0-9]\d{9}$').match(value):
        raise ValidationError('This is Not Valid Phone Number')


class NurseRegistration(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validation])
    Email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a valid Email')])

    class Meta:
        model = nurse
        fields = ('name', 'address', 'contact_no', 'Email', 'Hospital_name')

    def clean_email(self):
        Email = self.cleaned_data['Email']
        email_qs = nurse.objects.filter(Email=Email)
        if email_qs.exists():
            raise forms.ValidationError('This email already registered')
        return Email


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
        fields = ('subject', 'complaint', 'date')


class replyform(forms.ModelForm):
    class Meta:
        model = Complaint_Details
        fields = ('reply',)


class UserProfileUpdate(forms.ModelForm):
    contact_no = forms.CharField(validators=[phone_number_validation])
    Email = forms.CharField(validators=[
        RegexValidator(regex='^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Please Enter a valid Email')])

    class Meta:
        model = User
        fields = ('Name', 'Address', 'contact_no', 'Child_name', 'child_age', 'child_gender', 'Recent_vaccination')