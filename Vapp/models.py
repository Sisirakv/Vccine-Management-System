from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class User(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Address = models.TextField()
    contact_no = models.IntegerField()
    Child_name = models.CharField(max_length=20)
    child_age = models.IntegerField()
    child_gender = models.CharField(max_length=20)
    Recent_vaccination = models.DateField()

    def __str__(self):
        return self.Child_name


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    Email = models.EmailField()

    def __str__(self):
        return self.name


class nurse(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    Email = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    # log = models.ForeignKey(Login, on_delete=models.CASCADE)
    Hospital_name = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=50)
    vaccine_type = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)

    def __str__(self):
        return self.vaccine_name


class Reportcard(models.Model):
    Patient = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

    def __str__(self):
        return self.Patient, self.vaccine


class Schedule(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Appointment_Details')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    vaccine_name = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    # vaccinated = models.CharField(max_length=20)


class Complaint_Details(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    complaint = models.CharField(max_length=50)
    date = models.DateField()
    reply = models.CharField(max_length=50)
