# Generated by Django 4.0 on 2022-02-18 05:34

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=50)),
                ('vaccine_type', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_nurse', models.BooleanField(default=False)),
                ('is_user', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Address', models.TextField()),
                ('contact_no', models.IntegerField()),
                ('Child_name', models.CharField(max_length=20)),
                ('child_age', models.IntegerField()),
                ('child_gender', models.CharField(max_length=20)),
                ('Recent_vaccination', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Reportcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.user')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('Email', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
                ('Hospital_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('complaint', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('reply', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.schedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Appointment_Details', to='Vapp.user')),
                ('vaccine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vapp.vaccine')),
            ],
        ),
    ]
