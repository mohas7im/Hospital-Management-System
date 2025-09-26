from django.db import models
from django.contrib.auth.models import BaseUserManager,

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self,username,password=None):
        user=self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)



        return user
    
    def create_superuser(self,username,password):
        user=self.create_user(
            username=username,
            password=password,

        )
        permission=UserPermissions()

class UserAccount(models.Model):
    username=models.CharField(max_length=29,blank=True,null=True)
    password=models.CharField(max_length=29,blank=True,null=True)
class Department(models.Model):
    dep_name=models.CharField(max_length=200)
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr.' + self.doc_name + '(' + self.doc_spec + ')'


class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_age=models.IntegerField(default=0)
    p_phone=models.CharField(max_length=10)

    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    



class Userlogin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)


class Patient(models.Model):

    pname=models.CharField(max_length=70)
    page=models.IntegerField(default=0)
    pphone=models.CharField(max_length=15)
    paddress=models.CharField(max_length=100)
    ppin=models.CharField(max_length=20)
    pcity=models.CharField(max_length=10,blank=True,null=True)
    pstate=models.CharField(max_length=20,blank=True,null=True)
   




