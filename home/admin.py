from django.contrib import admin
# Register your models here.
from .models import Department, Doctors, Booking,Userlogin,Patient


admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Userlogin)



admin.site.register(Booking)

admin.site.register(Patient)


class PatientAdmin(admin.ModelAdmin):
    list_display=('patient name','patient age','patient phone','patient address','patient pin','patient city' 'patient state')