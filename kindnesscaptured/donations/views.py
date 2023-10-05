from rest_framework import generics
from .models import Donation
from .serializers import DonationSerializer
from rest_framework.permissions import IsAuthenticated

class DonationListCreateView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]

class DonationRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]