from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class DonatorUser(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    donator_groups = models.ManyToManyField(Group, related_name='donator_users', blank=True)
    donator_user_permissions = models.ManyToManyField(Permission, related_name='donator_users_permissions', blank=True)

class Donation(models.Model):
    USE_CHOICES = (
        ('new', 'New'),
        ('lightly used', 'Lightly Used'),
        ('old', 'Old'),
    )

    donator = models.ForeignKey(DonatorUser, on_delete=models.CASCADE)
    front_picture = models.ImageField(upload_to='donations/pictures')
    back_picture = models.ImageField(upload_to='donations/pictures')
    wear_tear = models.BooleanField(default=False)
    stain_odor_damage = models.BooleanField(default=False)
    use = models.CharField(max_length=50, choices=USE_CHOICES)
    ai_score = models.JSONField()
    approval = models.BooleanField(default=False)   
