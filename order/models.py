from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Reservation(models.Model):
    day = models.DateTimeField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)


class Order(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    pass
