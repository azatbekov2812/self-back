from django.shortcuts import render
from rest_framework import generics
from .models import Restaurant, RestaurantCategory, Food
from .serializers import OnlyRestaurantSerializer, OnlyRestaurantCategorySerializer, RestaurantSerializer


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


class FoodViews(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = ''
