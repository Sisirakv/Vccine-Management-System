
from django.urls import path

from Vapp import views, Admin_View
from Vapp.Admin_View import *

urlpatterns = [
 path('admin_page',views.ind,name="admin_page"),
 path('',views.home,name='home'),
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
]