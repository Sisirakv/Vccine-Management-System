
from django.urls import path

from Vapp import views, Admin_View, Nurse_View, User_View
from Vapp.Admin_View import *

urlpatterns = [
 path('admin_page',views.ind,name="admin_page"),
 path('',views.Home,name=''),
 path('login',views.login_views,name='login'),
 path('Nurse_regForm',views.nurse_register,name="Nurse_regForm"),
 path('User_regForm',views.user_register,name="User_regForm"),
 path('Add_Hosp',Admin_View.Add_Hospitals,name="Add_Hosp"),
 path('View_Nurse',Admin_View.viewnurse,name='View_Nurse'),
 path('View_User',Admin_View.viewuser, name='View_User'),
 path('View_Hospital',Admin_View.viewhospital, name='View_Hospital'),
 path('Add_Vaccine',Admin_View.Add_Vaccine,name="Add_Vaccine"),
 path('View_Vaccine',Admin_View.viewvaccine, name='View_Vaccine'),
 path('Add_ReportCard',Admin_View.Add_Reportcard,name="Add_ReportCard"),
 path('View_ReportCard',Admin_View.viewcard, name='View_ReportCard'),
 path('View_Appointments', Admin_View.viewappointments, name='View_Appointments'),
 path('View_Complaints', Admin_View.viewcomplaints, name='View_Complaints'),


 path('Nurse_page',views.nurseHome,name='Nurse_page'),
 path('User_Details',Nurse_View.userdetails,name='User_Details'),
 path('Hospital_Details', Nurse_View.hospitaldetails, name='Hospital_Details'),
 path('Add_appointments', Nurse_View.Add_Schedule, name='Add_appointments'),
 path('Add_complaints',Nurse_View.Add_Complaints,name='Add_complaints'),
 path('View_Appointments', Nurse_View.viewappointments, name='View_Appointments'),


 path('User_page',views.userHome,name='User_page'),
 path('User_profile', User_View.user_profile, name='User_profile'),
 path('User_Complaints',User_View.Add_Complaints,name='User_Complaints'),
]