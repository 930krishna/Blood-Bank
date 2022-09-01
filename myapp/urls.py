from django.urls import path
from . import views
urlpatterns = [
     path('home',views.home,name='home'),  
     path('',views.home,name='home'),  
    path('search',views.SearchDonor.as_view(),name='search'),
    path('userList',views.UserList.as_view(),name='userList'),


    path('addBank',views.AddBloodBank.as_view(),name='addBank'),
    path('bankList',views.BankList.as_view(),name='bankList'),
    path('updBank/<id>',views.UpdateBank.as_view(),name="updBank"),
    path('delBank/<id>',views.delBank,name='delBank'),

    path('addDonor',views.AddDonor.as_view(),name='addDonor'),
    path('donorList',views.donorList,name='donorList'),
    path('updDonor/<id>',views.UpdateDonor.as_view(),name="updDonor"),
    path('delDonor/<id>',views.DeleteDonor.as_view(),name="delDonor"),

    path('addReceiver',views.AddReceiver.as_view(),name='addReceiver'),
    path('receiverList',views.receiverList,name='receiverList'),
    path('updReceiver/<id>',views.UpdateReceiver.as_view(),name="updReceiver"),
    path('delReceiver/<id>',views.DeleteReceiver.as_view(),name="delReceiver"),

    path('register',views.Registration.as_view(),name='register'),
    path('logout',views.logouts,name='logout'),
]
