from django.urls import path

from .views import CustomObtainJwtIin

urlpatterns = [
    path('login/', CustomObtainJwtIin.as_view(), name='login_iin'),
]
