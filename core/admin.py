from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(RestaurantCategory)
admin.site.register(Restaurant)
admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(Sale)
