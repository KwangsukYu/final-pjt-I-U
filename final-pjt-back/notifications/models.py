from django.db import models
from django.conf import settings
from community.models import Article

# Create your models here.

class Notification(models.Model):

    TYPE_CHOICES = (
        ('like','Like'),
        ('unlike', 'Unlike'),
        ('comment','Comment'),
    )

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="creator")
    to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="to")
    Notification_type = models.CharField(max_length=30, choices=TYPE_CHOICES)
