from django.urls import path, include
from .views import UserRegistrationAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='api-register'),
]
