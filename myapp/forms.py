from urllib import request
from django import forms;
from .models import *



donstatus=[('available','Available'),('notavailable','Not Available')]
bloodqty=[('450 ML','450 ML'),('350 ML','350 ML'),('150 ML','150 ML')]
bgroup=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-')]
utypes=[('bloodbank','Bloodbank'),('donor','Donor'),('receiver','Receiver')]



class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    usertype=forms.CharField(widget=forms.Select(choices=utypes))
    class Meta:
        model=MyUser
        fields="__all__"

class BloodbankForm(forms.ModelForm):
    class Meta:
        model=Bloodbank
        fields={"bloodbankid","bbname","address","city","contact","email","contactPerson"}
    field_order = ['bloodbankid',"bbname","address","city","contact","email","contactPerson"]

class DonorForm(forms.ModelForm):
    status=forms.CharField(label="Status " ,widget=forms.Select(choices=donstatus))
    qty=forms.CharField(label="Quantity " ,widget=forms.Select(choices=bloodqty))
    bloodgroup=forms.CharField(widget=forms.Select(choices=bgroup))
    bloodCollectiondt=forms.CharField(widget=forms.DateInput)
    bloodExpirydt=forms.DateField()
    class Meta:
        model=Donor
        fields="__all__"

class ReceiverForm(forms.ModelForm):
    bloodgroup=forms.CharField(widget=forms.Select(choices=bgroup))
    class Meta:
        model=Receiver
        fields="__all__"

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=Complaint
        fields="__all__"
