from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import Department,Doctors,Booking,Patient,UserAccount

from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth.decorators import login_required



def loginornot(request):
    if not request.user.is_authenticated:
        return redirect('login')
def userlogin(request):
    if request.user and request.user.is_authenticated:
        return redirect("home")
 
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        UserAccount.objects.create(username=username,password=password,
        )

        user=authenticate(request,username=username,password=password)

       
        
        if user:
            auth_login(request,user)
            return redirect('home')  

         
            
        else:
            return HttpResponse("Not an user")
        

    return render(request,'login.html')    


@login_required(login_url=loginornot)
def index(request):
    return render(request, 'index.html')

@login_required(login_url=loginornot)
def about(request):
   
    return render(request,'about.html')
@login_required(login_url=loginornot)
def booking(request):
    if request.method=="POST":
        name=request.POST.get("name")
        bookingdate=request.POST.get("booking")
        age=request.POST.get("age")
        phoneno=request.POST.get("phone")
        doctor=request.POST.get("doctor")

        doc_obj=Doctors.objects.get(id=doctor)


        Booking.objects.create(
            p_name=name,
            p_age=age,
            booking_date=bookingdate,
            p_phone=phoneno,
            doc_name=doc_obj,
        )
        return redirect("booking")
    
    dict_doctors={
        'doctors':Doctors.objects.all()
    }
    
   
    return render(request,'booking.html',dict_doctors)
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



def user_logout(request):
    logout(request)
    return redirect('login') 



def dashboardhome(request):
    return render(request,'dashboardhome.html')

def dashboardpatient(request):


    return render(request,'dashboardpatient.html')

def dashboardbooking(request):
    dict_bookingdash={
        'booking':Booking.objects.all()
    }
    return render(request,'dashboardbooking.html',dict_bookingdash)


def dashboardexpense(request):
    return render(request,'dashboardexpense.html')

def dashboardDelete(request,id):
    row = Booking.objects.get(id=id)
    row.delete()
    return redirect('dashboardbooking')

def UpdateBooking(request,id):
    newrow=Booking.objects.get(id=id)
    
    if request.method == "POST":
        print("okook")
        x=request.POST.get('p_name')
        y=request.POST.get('p_phone')      
        newrow.p_name=x
        newrow.p_phone=y
        newrow.save()

        return redirect('dashboardbooking')

    return render(request,'dashboardbooking.html',{'row':newrow})


def dashboarddoctor(request):
     
    if request.method=="POST":
        
        doctorname=request.POST.get("doctorname")
        doctorspec=request.POST.get("doctorspec")
        depname=request.POST.get("doctordepartment")
        docimage=request.FILES.get("doctorprofile")

        
        department_obj=Department.objects.get(id=depname)

        Doctors.objects.create(
            doc_name=doctorname,
            doc_spec=doctorspec,
            dep_name=department_obj,
            doc_image=docimage,


        )

        return redirect('dashboarddoctor')
    
   
        
    

    
    dict_doctordash={
        'doctors':Doctors.objects.all(),
        'department':Department.objects.all()
    }
   
    
    return render(request,"dashboarddoctor.html",dict_doctordash)

def dashboarddoctordelete(request,id):
    
    row=Doctors.objects.get(id=id)
    row.delete()
    return redirect('dashboarddoctor')
# def dashboarddoctorupdate(request,id):
#    row=Doctors.objects.get(id=id)
#    if request.method=="POST":
#          x=request.POST.get("doctorname")
#          y=request.POST.get("doctorspec")
#          z=request.POST.get("doctordepartment")
#          w=request.POST.get("doctorprofile")



def patient(request):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        phone=request.POST.get("phoneno")
        address=request.POST.get("address")
        pin=request.POST.get("pin")
        city=request.POST.get("city")

        

        patient=Patient.objects.create(
            pname=name,
            page=age,
            pphone=phone,
            paddress=address,
            ppin=pin,
            pcity=city,
        )


       
        return redirect('patient')
    
   
    

    return render(request,'patient.html')   


