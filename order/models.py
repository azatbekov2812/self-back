from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
from django.template.defaulttags import now

from core.models import Restaurant

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
    products = ArrayField(models.IntegerField(), default=[])
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-create_date',)


class Booking(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='bookings')
    bookDate = models.DateField()
    bookTime = models.TimeField()
    participants = ArrayField(models.IntegerField(), default=[])
    peopleCount = models.IntegerField(null=True, blank=True)
    table = models.IntegerField()
    bookComment = models.CharField(max_length=255, default='', blank=True, null=True)
    products = ArrayField(models.IntegerField(), default=[])
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create_date',)
