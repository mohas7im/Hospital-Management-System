from django.urls import path, include
from .views import *
urlpatterns=[
    
    path('', userlogin,name='login'),
    path('home/', index,name='home'),
    path('about/', about,name='about'),
    path('booking/', booking,name='booking'),
    path('doctors/', doctors,name='doctors'),
    path('contact/', contact,name='contact'),
    path('department/', department,name='department'),
    path('logout/',user_logout,name='logout'), 
    path('auth-check/',loginornot),
    path('dashboard',dashboard)
   


    

    
    

    
]