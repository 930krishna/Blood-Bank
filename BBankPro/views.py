from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from myapp.models import *
from django.core.paginator import Paginator
import random

def index(request):
    return render(request,'home.html')

class BloodBanks(View):
    def get(self,request):
        data=Bloodbank.objects.all()
        mydata = BloodBanks.common(data,request)
        return render(request,'bloodbank.html',{'mydata':mydata})
    def post(self,request):
        city=request.POST['city']
        if city:
            data=Bloodbank.objects.filter(city__exact=city) 
        else:
            data=Bloodbank.objects.all()
        mydata = BloodBanks.common(data,request)  
        return render(request,'bloodbank.html',{'mydata':mydata, 'city': city})
    def common(data,request):
        p = Paginator(data, 10)
        page_number = request.GET.get('page')
        return p.get_page(page_number)

class Complaints(View):
    def get(self,request):
        data=Complaint.objects.all()
        mydata = Complaints.common(data,request)
        return render(request,'complaint.html',{'mydata':mydata})
    def post(self,request):
        comp_no=request.POST['comp_no']
        if comp_no:
            data=Complaint.objects.filter(comp_no__exact=comp_no) 
        else:
            data=Complaint.objects.all()
        mydata = Complaints.common(data,request)  
        return render(request,'complaint.html',{'mydata':mydata, 'comp_no': comp_no})
    def common(data,request):
        p = Paginator(data, 10)
        page_number = request.GET.get('page')
        return p.get_page(page_number)

class AddComplaints(View):
    def get(self,request):
        data=Bloodbank.objects.all()
        comp_no=AddComplaints.generate_comp_no()
        return render(request,'addComplaints.html',{"mydata": data, "comp_no": comp_no})        
    def post(self,request):
            comp_no=request.POST['comp_no'];
            comp_name=request.POST['title'];
            comp_phone=request.POST['contact'];
            comp_msg=request.POST['message'];
            status="Hold";
            username_id="admin"
            p=Complaint(comp_no=comp_no,comp_name=comp_name,comp_phone=comp_phone,comp_msg=comp_msg,status=status,username_id=username_id)
            p.save()
            return redirect('complaints')
    def generate_comp_no():
        return random.randint(1000,9999)

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        unm=request.POST['unm']
        pwd=request.POST['pass']
        userdata=MyUser.objects.filter(username__exact=unm).filter(password__exact=pwd)
        if userdata:
            for user in userdata:
                if user.usertype == "bloodbank":
                    obj=get_object_or_404(Bloodbank,username_id=user.username)
                    request.session['bloodbankid']=obj.bloodbankid                    
                request.session['utype']=user.usertype
                request.session['uname']=user.firstname+" "+user.lastname
                request.session['username']=user.username
                request.session['created_by']=user.created_by
            return redirect('home')
        else:
            return HttpResponse("<h3>Invalid User Details....</h3>")        