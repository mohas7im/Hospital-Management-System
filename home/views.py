from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Department,Doctors
from .forms import BookingForm
from django.contrib.auth import authenticate,login as auth_login





# Create your views here.
def index(request):
    if not request.user and not request.user.is_authenticated:
        return redirect('login')
    


   


    return render(request, 'index.html')

def about(request):
    entries = [
        {"date": "2025-09-01", "description": "Purchase Office Supplies", "debit": 500, "credit": 0},
        {"date": "2025-09-02", "description": "Customer Payment", "debit": 0, "credit": 1200},
        {"date": "2025-09-05", "description": "Electricity Bill", "debit": 800, "credit": 0},
        {"date": "2025-09-07", "description": "Service Income", "debit": 0, "credit": 2000},
    ]

    # Calculate totals
    total_debit = sum(item["debit"] for item in entries)
    total_credit = sum(item["credit"] for item in entries)
    balance = total_credit - total_debit   # credit - debit

    context = {
        "entries": entries,
        "total_debit": total_debit,
        "total_credit": total_credit,
        "balance": balance,
    }
    return render(request,'about.html',context)

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

def doctors(request):
    dict_doctors={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doctors)  
    
 
def contact(request):
    return render(request,'contact.html')

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
    
