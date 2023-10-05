from django.urls import path 
from .views import DonationListCreateView, DonationRetrieveUpdateView

app_name = 'donations'

urlpatterns = [
    path('', DonationListCreateView.as_view(), name='donations-list-create'),
    path('<int:pk>/', DonationRetrieveUpdateView.as_view(), name='donations-retrieve-update'),
]