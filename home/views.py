from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Department,Doctors
from .forms import BookingForm
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required



def loginornot(request):
    if not request.user.is_authenticated:
        return redirect('login')
    


@login_required(login_url=loginornot)
def index(request):
    return render(request, 'index.html')

@login_required(login_url=loginornot)
def about(request):
   
    return render(request,'about.html')
@login_required(login_url=loginornot)
def booking(request):
    
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)
@login_required(login_url=loginornot)
def doctors(request):
    dict_doctors={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doctors)  
    
@login_required(login_url=loginornot)
def contact(request):
    return render(request,'contact.html')
@login_required(login_url=loginornot)
def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)

def userlogin(request):
    if request.user and request.user.is_authenticated:
        return redirect("home")
 
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)
        
        if user:
            auth_login(request,user)
            return redirect('home')  

         
            
        else:
            return HttpResponse("Not an user")
        

    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('login') 



def dashboard(request):
    return render(request,'dashboard.html')

