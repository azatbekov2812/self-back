from django.urls import path

from .views import CustomObtainJwtIin, UserViewSet

urlpatterns = [
    path('login/', CustomObtainJwtIin.as_view(), name='login_iin'),
    path('profile/<int:pk>/', UserViewSet.as_view(), name='login_iin'),
]
