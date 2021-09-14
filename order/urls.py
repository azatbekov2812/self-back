from django.urls import path

from .views import *

urlpatterns = [
    path('delivery/', OrderView.as_view()),
    path('delivery/<int:pk>/', OrderDetailView.as_view()),
    path('booking/', BookView.as_view()),
    path('booking/<int:pk>/', BookDetailView.as_view()),
]
