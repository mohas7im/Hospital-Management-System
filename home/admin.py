from django.contrib import admin
# Register your models here.
from .models import Department, Doctors, Booking,Userlogin


admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Userlogin)



admin.site.register(Booking)

