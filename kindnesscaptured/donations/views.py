from rest_framework import viewsets
from .models import DonatorUser, Donation
from .serializers import DonatorUserSerializer, DonationSerializer

class DonatorUserViewSet(viewsets.ModelViewSet):
    queryset = DonatorUser.objects.all()
    serializer_class = DonatorUserSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer