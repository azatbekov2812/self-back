from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('restaurants-categories/', RestaurantCategoryViews.as_view(), name='restaurants'),
    path('restaurants/', RestaurantViews.as_view(), name='restaurants'),
    path('restaurants/<int:restaurant_id>/food-categories/', RestaurantViews.as_view(), name='restaurants'),
]
