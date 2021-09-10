from rest_framework import generics
from .models import Restaurant, RestaurantCategory, Food, FoodCategory
from .serializers import OnlyRestaurantCategorySerializer, RestaurantSerializer, \
    FoodSerializer, FoodCategorySerializer
from rest_framework import generics

from .models import *
from .serializers import *


# Create your views here.
class SaleViews(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class RestaurantCategoryViews(generics.ListAPIView):
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
