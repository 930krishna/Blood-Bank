from rest_framework import generics
from myapp.models import *
from .serializers import *

class BloodBankListView(generics.ListCreateAPIView):
    queryset=Bloodbank.objects.all()
    serializer_class=BloodbankSerializer


class BloodBankDetailsView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Bloodbank.objects.all()
     serializer_class=BloodbankSerializer

class DonorListView(generics.ListCreateAPIView):
    queryset=Donor.objects.all()
    serializer_class=DonorSerializer


class DonorDetailsView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Donor.objects.all()
     serializer_class=DonorSerializer

class ReceiverListView(generics.ListCreateAPIView):
    queryset=Receiver.objects.all()
    serializer_class=ReceiverSerializer


class ReceiverDetailsView(generics.RetrieveUpdateDestroyAPIView):
     queryset=Receiver.objects.all()
     serializer_class=ReceiverSerializer
