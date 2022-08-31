from django.urls import path
from . import views

urlpatterns = [
    path('bloodbank',views.BloodBankListView.as_view()),
    path('bloodbank/<int:pk>',views.BloodBankDetailsView.as_view()),

    path('donor',views.DonorListView.as_view()),
    path('donor/<int:pk>',views.DonorDetailsView.as_view()),

    path('receiver',views.ReceiverListView.as_view()),
    path('receiver/<int:pk>',views.ReceiverDetailsView.as_view()),

]
