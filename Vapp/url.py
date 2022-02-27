
from django.urls import path

from Vapp import views, Admin_View, Nurse_View, User_View
from Vapp.Admin_View import *

urlpatterns = [
 path('admin_page',views.ind,name="admin_page"),
 path('',views.Home,name=''),
 path('login',views.login_views,name='login'),
 path('logout_view',views.logout_view, name='logout_view'),
 path('Nurse_regForm',views.nurse_register,name="Nurse_regForm"),
 path('User_regForm',views.user_register,name="User_regForm"),
 path('Add_Hosp',Admin_View.Add_Hospitals,name="Add_Hosp"),
 path('View_Nurse',Admin_View.viewnurse,name='View_Nurse'),
 path('View_User',Admin_View.viewuser, name='View_User'),
 path('View_Hospital',Admin_View.viewhospital, name='View_Hospital'),
 path('Add_Vaccine',Admin_View.Add_Vaccine,name="Add_Vaccine"),
 path('Approving', Admin_View.appointments, name="Approving"),
 path('View_Vaccine',Admin_View.viewvaccine, name='View_Vaccine'),
 path('View_Appointments', Admin_View.viewappointments, name='View_Appointments'),
 path('View_Complaints', Admin_View.viewcomplaints, name='View_Complaints'),
 path('Reply', Admin_View.reply_complaint, name='Reply'),
 path('Delete_Hospital/<int:id>/', Admin_View.hospitalDelete, name='Delete_Hospital'),
 path('Update_Hospital/<int:id>/', Admin_View.hospitalUpdate, name='Update_Hospital'),
 path('Delete_Vaccine/<int:id>/', Admin_View.vaccineDelete, name='Delete_Vaccine'),
 path('Update_Vaccine/<int:id>/', Admin_View.vaccineUpdate, name='Update_Vaccine'),

 path('Nurse_page',views.nurseHome,name='Nurse_page'),
 path('User_Details',Nurse_View.userdetails,name='User_Details'),
 path('Hospital_Details', Nurse_View.hospitaldetails, name='Hospital_Details'),
 path('Add_ReportCard', Nurse_View.Add_Reportcard, name="Add_ReportCard"),
 path('View_ReportCard', Nurse_View.viewcard, name='View_ReportCard'),
 path('Add_appointments', Nurse_View.Add_Schedule, name='Add_appointments'),
 path('Add_complaints',Nurse_View.Add_Complaints,name='Add_complaints'),
 path('Appointments_Details', Nurse_View.appointmentdetails, name='Appointments_Details'),
 path('Schedule_Details', Nurse_View.viewschedules, name='Schedule_Details'),
 path('Vaccine_Details', Nurse_View.vaccinedetails, name='Vaccine_Details'),
 path('Complaint_Details', Nurse_View.viewcomplaints_nurse, name='Complaint_Details'),
 path('Delete_Appointments/<int:id>/',Nurse_View.appointmentDelete,name='Delete_Appointments'),
 path('Update_Appointments/<int:id>/', Nurse_View.scheduleUpdate, name='Update_Appointments'),
 path('Update_Complaint/<int:id>/', Nurse_View.complaintUpdate, name='Update_Complaint'),
 path('Delete_Complaint/<int:id>/', Nurse_View.complaintDelete, name='Delete_Complaint'),
 path('Delete_ReportCard/<int:id>/', Nurse_View.reportcardDelete, name='Delete_ReportCard'),
 path('Update_ReportCard/<int:id>/', Nurse_View.reportcardUpdate, name='Update_ReportCard'),


 path('User_page',views.userHome,name='User_page'),
 path('User_profile', User_View.Userprofile, name='User_profile'),
 path('User_Complaints',User_View.Add_Complaints,name='User_Complaints'),
 path('Fix_Schedule', User_View.fixschedules, name='Fix_Schedule'),
 path('Your_Complaints', User_View.compaintview, name='Your_Complaints'),
 path('Take_Appointment/<int:user_id>/', User_View.take_appointment, name='Take_Appointment'),
 path('Delete_Complaint_User/<int:id>/', User_View.complaintDelete_User, name='Delete_Complaint_User'),
 path('Update_Complaint_User/<int:id>/', User_View.complaintUpdate_user, name='Update_Complaint_User'),
 path('Report', User_View.report,name='Report'),


]