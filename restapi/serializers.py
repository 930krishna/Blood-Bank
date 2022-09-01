from dataclasses import field
from rest_framework import serializers
from myapp.models import *

class BloodbankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bloodbank
        fields="__all__"

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields="__all__"

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receiver
        fields="__all__"                
