from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Login)

admin.site.register(User)
admin.site.register(nurse)
admin.site.register(Reportcard)
# admin.site.register(U_Complaints)
# admin.site.register(N_Complaints)
admin.site.register(Hospital)
admin.site.register(Vaccine)
admin.site.register(Schedule)
admin.site.register(Appointment)