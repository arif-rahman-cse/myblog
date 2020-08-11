from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.account.serializers import UserRegistrationSerializer


class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


"""
@api_view(['POST', ])
def api_registration_view(request):
    if request == 'POST':  # Checking Is request is POST
        serializer = UserRegistrationSerializer(data=request.DATA)  # Passing registration data to RegistrationSerializer
        data = {}  # Define data variable for storing response
        if serializer.is_valid():  # Checking Data is valid
            user = serializer.save()  # calling override save function
            data['response'] = 'Successfully registered a new user.'  # assign success value to data variable
            data['email'] = user.email  # assign email to data variable
            data['username'] = user.username  # assign username to data variable
        else:
            data = serializer.errors
        return Response(data)
"""
