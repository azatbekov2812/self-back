from django.urls import path

from .views import *

urlpatterns = [
    path('login/', CustomObtainJwtIin.as_view(), name='login_iin'),
    # path('profile/<int:pk>/', UserViewSet.as_view(), name='login_iin'),
    path('profile/<int:pk>/', user_profile, name='user_profile'),
]
