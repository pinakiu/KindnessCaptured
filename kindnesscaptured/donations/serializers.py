from rest_framework import serializers
from .models import DonatorUser, Donation

class DonatorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatorUser
        fields = ['id', 'username', 'email', 'name', 'phone', 'address', 'is_active', 'donator_groups', 'donator_user_permissions']

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'donator', 'front_picture', 'back_picture', 'wear_tear', 'stain_odor_damage', 'use', 'ai_score', 'approval']