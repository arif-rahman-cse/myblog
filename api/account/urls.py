from django.urls import path, include
from .views import UserRegistrationAPIView, UserLoginAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='api-register'),
    path('login/', UserLoginAPIView.as_view(), name='api-login'),
]
