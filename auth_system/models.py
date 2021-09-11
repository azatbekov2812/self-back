from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, related_name='profile')
    avatar = models.ImageField(upload_to='pictures/avatar/', max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
