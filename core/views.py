from rest_framework import generics, status
from rest_framework.decorators import api_view

from .models import Restaurant, RestaurantCategory, Food, FoodCategory
from .serializers import OnlyRestaurantCategorySerializer, RestaurantSerializer, \
    FoodSerializer, FoodCategorySerializer
from rest_framework import generics
from rest_framework.response import Response
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
            return Restaurant.objects.filter(restaurant_category=category_id)
        return Restaurant.objects.all()


class RestaurantDetailViews(generics.RetrieveAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    # def get_queryset(self):
    #     category_id = self.request.query_params.get('category_id')
    #     if category_id:
    #         return Restaurant.objects.filter(restaurant_category=category_id)
    #     return Restaurant.objects.all()


class FoodCategoryViews(generics.ListAPIView):
    serializer_class = FoodCategorySerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['restaurant_id']
        return FoodCategory.objects.filter(restaurants=restaurant_id)


class FoodViews(generics.ListAPIView):
    serializer_class = FoodSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs.get('restaurant_id')
        food_category_id = self.kwargs.get('food_category_id')
        if food_category_id:
            return Food.objects.filter(restaurant=restaurant_id, food_category=food_category_id)
        return Food.objects.filter(restaurant=restaurant_id)


@api_view(['GET'])
def food_detail(request, pk):
    food = Food.objects.get(pk=pk)
    data = FoodSerializer(food).data
    return Response(data, status=status.HTTP_200_OK)
