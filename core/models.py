from django.db import models


# Create your models here.

class RestaurantCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='pictures/restaurants/', max_length=255, blank=True, null=True)
    restaurant_category = models.ManyToManyField(RestaurantCategory, blank=True, null=True)
    food_category = models.ManyToManyField('FoodCategory', blank=True, null=True, related_name='restaurants')

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_foods')
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='category_foods')
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='pictures/foods/', max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.food_category) + ' -- ' + self.name


class Sale(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(max_length=255, blank=True, null=True)
    discount = models.IntegerField(default=0)
