from django.db import models


# Create your models here.

class RestaurantCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    avatar = models.ImageField(max_length=255, blank=True, null=True)
    category = models.ManyToManyField(RestaurantCategory)

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='food_categories')

    def __str__(self):
        return str(self.restaurant) + ' -- ' + self.name


class Food(models.Model):
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='foods')
    name = models.CharField(max_length=255)
    avatar = models.ImageField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.food_category) + ' -- ' + self.name


class Sale(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(max_length=255, blank=True, null=True)
    discount = models.IntegerField(default=0)