# Generated by Django 4.0 on 2022-02-09 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vapp', '0005_alter_appointment_schedule_alter_complaint_complaint_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Complaint',
        ),
    ]
