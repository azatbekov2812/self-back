from django.urls import path

from .views import *

urlpatterns = [
    path('delivery/', OrderView.as_view()),
    path('booking/', BookView.as_view()),
]
