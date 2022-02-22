from django import forms
from django_filters import CharFilter

from Vapp.models import User, nurse, Hospital, Vaccine, Appointment_Details, Schedule
import django_filters


class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('name',)


class NurseFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = nurse
        fields = ('name',)


class HospitalFilter(django_filters.FilterSet):
    name = CharFilter(field_name='place', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Hospital Name', 'class': 'form-control'}))

    class Meta:
        model = Hospital
        fields = ('name',)


class VaccineFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Vaccine Name', 'class': 'form-control'}))

    class Meta:
        model = Vaccine
        fields = ('name',)


class ScheduleFilter(django_filters.FilterSet):
    name = CharFilter(field_name='hospital', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Hospital', 'class': 'form-control'}))

    class Meta:
        model = Schedule
        fields = ('hospital',)


class PlaceFilter(django_filters.FilterSet):
    schedule__hospital = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Hospital', 'class': 'form-control'}))

    class Meta:
        model = Appointment_Details
        fields = ('schedule__hospital',)
