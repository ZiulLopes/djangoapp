from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(default='')
    website = models.CharField(default='')
    phone = models.IntegerField(default=0)