# Generated by Django 4.0 on 2022-02-04 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vapp', '0008_remove_hospital_contact_hospital_contact_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportcard',
            name='patient',
        ),
        migrations.AddField(
            model_name='reportcard',
            name='Patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Vapp.user'),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='Approval_status',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaccine',
            name='Description',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportcard',
            name='vaccine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Vapp.vaccine'),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='vaccine_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='vaccine_type',
            field=models.CharField(max_length=50),
        ),
    ]
