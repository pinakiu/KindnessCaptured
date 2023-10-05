from django.db import models
from users.models import EmployeeUser, DonaterUser

class Donation(models.Model):
    USE_CHOICES = (
        ('new', 'New'),
        ('lightly used', 'Lightly Used'),
        ('old', 'Old'),
    )

    donater = models.ForeignKey(DonaterUser, on_delete=models.CASCADE)
    front_picture = models.ImageField(upload_to='donations/pictures')
    back_picture = models.ImageField(upload_to='donations/pictures')
    wear_tear = models.BooleanField(default=False)
    stain_odor_damage = models.BooleanField(default=False)
    use = models.CharField(max_length=50, choices=USE_CHOICES)
    ai_score = models.JSONField()
    approval = models.BooleanField(default=False)

