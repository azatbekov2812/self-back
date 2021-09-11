from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    avatar = models.ImageField(upload_to='pictures/avatar/', max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
