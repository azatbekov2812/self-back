from django.urls import path

from .views import *

urlpatterns = [
    path('sales/', RestaurantCategoryViews.as_view(), name='restaurants'),  # all category restaurants
    path('restaurants-categories/', RestaurantCategoryViews.as_view(), name='restaurants'),  # all category restaurants
    path('restaurants/', RestaurantViews.as_view(), name='restaurants'),  # all restaurants with params 'category_id'
    path('restaurants/<int:restaurant_id>/food-categories/', FoodCategoryViews.as_view(), name='food_categories'),
    # all food category one restaurants
    path('restaurants/<int:restaurant_id>/food-categories/foods/', FoodViews.as_view(),
         name='restaurants'),  # all foods one category
    path('restaurants/<int:restaurant_id>/food-categories/<int:food_category_id>/', FoodViews.as_view(),
         name='foods_one_categories'),  # all foods one category
]
