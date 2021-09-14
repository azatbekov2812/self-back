from rest_framework import serializers

from .models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'creator': {'required': True},
            'products': {'required': True},
        }


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {
            'creator': {'required': True},
            'restaurant': {'required': True},
            'bookDate': {'required': True},
            'bookTime': {'required': True},
            'table': {'required': True},
        }
