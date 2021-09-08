from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Restaurant, RestaurantCategory, Food


class OnlyRestaurantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCategory
        fields = '__all__'


class OnlyRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    category = OnlyRestaurantCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
