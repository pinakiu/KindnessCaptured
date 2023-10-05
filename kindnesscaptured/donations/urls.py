from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DonatorUserViewSet, DonationViewSet

app_name = 'donations'

router = DefaultRouter()
router.register(r'donators', DonatorUserViewSet)
router.register(r'donations', DonationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]