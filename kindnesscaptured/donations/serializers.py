from rest_framework import serializers
from .models import Donation
from django.conf import settings

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
