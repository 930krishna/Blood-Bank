from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import *
from .forms import *
from django.contrib.auth import logout


def home(request):
    return render(request,'home.html')

class AddBloodBank(View):
    def get(self,request):
        myform=BloodbankForm()
        username=request.session['username']
        return render(request,'addBank.html',{'myform':myform,'username':username})        
    def post(self,request):
        unm=request.session['username']
        # print("The username is : ",unm)
        myform=BloodbankForm(request.POST)
        if myform.is_valid():
            bloodbankid=myform.cleaned_data['bloodbankid']
            bbname=myform.cleaned_data['bbname']
            address=myform.cleaned_data['address']
            city=myform.cleaned_data['city']
            contact=myform.cleaned_data['contact']
            email=myform.cleaned_data['email']
            contactPerson=myform.cleaned_data['contactPerson']
            username=unm
            bank=Bloodbank(bloodbankid,bbname,address,city,contact,email,contactPerson,username)
            bank.save()
            return redirect('home')
        else:
            return HttpResponse("<h5>Data could not be added...")          
 
def bankList(request):
    data=Bloodbank.objects.all()
    return render(request,'bankList.html',{'mydata':data})

class UpdateBank(View):
    def get(self,request,id):
        obj=get_object_or_404(Bloodbank,bloodbankid=id)
        myform=BloodbankForm(instance=obj)
        return render(request,'updBank.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(Bloodbank,bloodbankid=id)
        myform=BloodbankForm(request.POST,instance=obj)
        if myform.is_valid():
            myform.save()
            return redirect('bankList')

class DeleteBank(View):
    def get(self,request,id):
        obj=get_object_or_404(Bloodbank,bloodbankid=id)
        myform=BloodbankForm(instance=obj)
        return render(request,'delBank.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(Bloodbank,bloodbankid=id)
        obj.delete()
        return redirect('bankList')        
    
class AddDonor(View):
    def get(self,request):
        myform=DonorForm()
        return render(request,'addDonor.html',{'myform':myform})        
    def post(self,request):
        myform=DonorForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('home')
        else:
            return HttpResponse("<h5>Data could not be added...")

class UpdateDonor(View):
    def get(self,request,id):
        obj=get_object_or_404(Donor,donorid=id)
        myform=DonorForm(instance=obj)
        return render(request,'updDonor.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(Donor,donorid=id)
        myform=DonorForm(request.POST,instance=obj)
        if myform.is_valid():
            myform.save()
            return redirect('donorList')

class DeleteDonor(View):
    def get(self,request,id):
        obj=get_object_or_404(Donor,donorid=id)
        myform=DonorForm(instance=obj)
        return render(request,'delDonor.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(Donor,donorid=id)
        obj.delete()
        return redirect('donorList') 

def donorList(request):
    username=request.session['username']
    data=Donor.objects.filter(username__iexact=username)
    return render(request,'donorList.html',{'mydata':data})

class AddReceiver(View):
    def get(self,request):
        myform=ReceiverForm()
        return render(request,'addReceiver.html',{'myform':myform})        
    def post(self,request):
        myform=ReceiverForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('home')
        else:
            return HttpResponse("<h5>Data could not be added...")          

class UpdateReceiver(View):
    def get(self,request,id):
        obj=get_object_or_404(Receiver,receiverid=id)
        myform=ReceiverForm(instance=obj)
        return render(request,'updReceiver.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(Receiver,receiverid=id)
        myform=ReceiverForm(request.POST,instance=obj)
        if myform.is_valid():
            myform.save()
            return redirect('receiverList')

class DeleteReceiver(View):
    def get(self,request,id):
        obj=get_object_or_404(Receiver,receiverid=id)
        myform=ReceiverForm(instance=obj)
        return render(request,'delReceiver.html',{'myform':myform})
    def post(self,request,id):
        obj=get_object_or_404(Receiver,receiverid=id)
        obj.delete()
        return redirect('receiverList') 

def receiverList(request):
    data=Receiver.objects.all()
    return render(request,'receiverList.html',{'mydata':data})

class SearchDonor(View):
    def get(self,request):
        return render(request,'search.html')
    def post(self,request):
        bg=request.POST['bg']
        ct=request.POST.get('ct')
        if(bg and not ct):
            data=Donor.objects.filter(bloodgroup__iexact=bg)
        elif(ct and not bg):
            data=Donor.objects.filter(city__iexact=ct)
        elif(bg and ct):
            data=Donor.objects.filter(bloodgroup__iexact=bg).filter(city__iexact=ct)
        else:
            data=Donor.objects.all()
        return render(request,'donordata.html',{'mydata':data})


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        unm=request.POST['unm']
        pwd=request.POST['pass']
        userdata=MyUser.objects.filter(username__exact=unm).filter(password__exact=pwd)
        if userdata:
            for user in userdata:
                request.session['utype']=user.usertype
                request.session['uname']=user.firstname+" "+user.lastname
                request.session['username']=user.username
            return redirect('home')
        else:
            return HttpResponse("<h3>Invalid User Details....</h3>")
        

class Registration(View):
    def get(self,request):
        myform=UserForm()
        return render(request,'register.html',{'myform':myform})
    def post(self,request):
        myform=UserForm(request.POST)
        if myform.is_valid():
            myform.save()
        return redirect('logins')

def logouts(request):
        logout(request)
        return redirect('home')