from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Reservation(models.Model):
    day = models.DateTimeField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)


class Order(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    streetName = models.CharField(max_length=255, default='', blank=True)
    streetHouse = models.CharField(max_length=255, default='', blank=True)
    apartmentOrOffice = models.CharField(max_length=255, default='', blank=True)
    entrance = models.CharField(max_length=255, default='', blank=True)
    floor = models.CharField(max_length=255, default='', blank=True)
    addressComment = models.CharField(max_length=255, default='', blank=True)
    deliveryTime = models.CharField(max_length=255, default='', blank=True)
    payment_type = models.CharField(max_length=255, default='', blank=True)
    peopleCount = models.CharField(max_length=255, default='', blank=True)
    orderComment = models.CharField(max_length=255, default='', blank=True)
