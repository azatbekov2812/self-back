from django.shortcuts import render
from rest_framework import generics
from .models import Restaurant, RestaurantCategory, Food, FoodCategory
from .serializers import OnlyRestaurantSerializer, OnlyRestaurantCategorySerializer, RestaurantSerializer, \
    FoodSerializer, FoodCategorySerializer


# Create your views here.


class RestaurantCategoryViews(generics.ListCreateAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = OnlyRestaurantCategorySerializer


class RestaurantViews(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            return Restaurant.objects.filter(category__in=category_id)
        return Restaurant.objects.all()


class FoodCategoryViews(generics.ListAPIView):
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return FoodCategory.objects.filter(restaurant_id=restaurant_id)


class FoodViews(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        food_category_id = self.kwargs.get('food_category_id')
        if food_category_id:
            return Food.objects.filter(food_category=food_category_id)
        return Food.objects.filter(food_category__restaurant__id=restaurant_id)
