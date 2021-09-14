from django.contrib import admin

# Register your models here.
from .models import Order, Booking

admin.site.register(Order)
admin.site.register(Booking)
