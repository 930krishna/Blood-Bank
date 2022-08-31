
from django.db import models


class MyUser(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    password=models.CharField(max_length=500)
    usertype=models.CharField(max_length=20, default='Guest')
    created_by=models.CharField(max_length=20,default='admin')
    def __str__(self):
        return self.username

class Bloodbank(models.Model):
    bloodbankid=models.AutoField(primary_key=True)
    bbname=models.CharField(max_length=50)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    contact=models.CharField(max_length=10)
    email=models.EmailField()
    contactPerson=models.CharField(max_length=30)
    username=models.ForeignKey("MyUser", on_delete=models.CASCADE)
    def __str__(self):
        return self.bbname+"-"+self.city

class Donor(models.Model):
    donorid=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=50)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    contact=models.CharField(max_length=10)
    bloodgroup=models.CharField(max_length=4)
    qty=models.CharField(max_length=6)
    bloodbagno=models.IntegerField()
    bloodCollectiondt=models.DateField()
    bloodExpirydt=models.DateField()
    bloodbankid=models.ForeignKey("Bloodbank",on_delete=models.CASCADE)
    status=models.CharField(max_length=20)
    username=models.ForeignKey("MyUser", on_delete=models.CASCADE)
    def __str__(self):
        return self.dname+"-"+self.bloodgroup

class Receiver(models.Model):
    receiverid=models.AutoField(primary_key=True)
    rcname=models.CharField(max_length=50)
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    bloodgroup=models.CharField(max_length=4)
    qty_req=models.IntegerField()
    alloted_bloodbagno=models.IntegerField()
    request_no=models.IntegerField()
    request_dt=models.DateField()
    request_status=models.CharField(max_length=20)
    hospital=models.CharField(max_length=50)
    amount=models.IntegerField()
    bloodbankid=models.ForeignKey("Bloodbank",on_delete=models.CASCADE)
    username=models.ForeignKey("MyUser", on_delete=models.CASCADE)
    def __str__(self):
        return self.rcname+"-"+self.bloodgroup+"-"+self.city

class Complaint(models.Model):
    comp_id=models.AutoField(primary_key=True)
    comp_no=models.IntegerField()
    comp_name=models.CharField(max_length=255)
    comp_phone=models.CharField(max_length=10)
    comp_msg=models.CharField(max_length=500)
    status=models.CharField(max_length=20)
    username=models.ForeignKey("MyUser", on_delete=models.CASCADE)
    def __str__(self):
        return self.comp_name+"-"+self.comp_phone+"-"+self.status
