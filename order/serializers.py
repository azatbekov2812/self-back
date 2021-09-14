from rest_framework import serializers

from core.serializers import FoodSerializer
from .models import *


class CustomSerializer(serializers.ModelSerializer):
    pass


class OrderSerializer(serializers.ModelSerializer):
    get_products = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {
            'creator': {'required': True},
            'products': {'required': True},
        }


class BookingSerializer(serializers.ModelSerializer):
    get_products = FoodSerializer(many=True, read_only=True)

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
