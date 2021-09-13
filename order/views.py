from django.shortcuts import render
from rest_framework import generics, status
from .models import *
from .serializers import *


# Create your views here.
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
