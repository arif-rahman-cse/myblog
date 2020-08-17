from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from api.account.serializers import UserRegistrationSerializer, UserLoginSerializer


class UserRegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):  # <- here i forgot self
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        user_id = serializer.instance.id
        username = serializer.instance.username
        email = serializer.instance.email
        return Response({'id': user_id, 'username': username, 'email': email, 'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = self.request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)  # I'm getting this response
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


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

"""
def post(self, request, *args, **kwargs):
    data = request.data
    serializer = UserLoginSerializer(data)
    if serializer.is_valid():
        new_data = serializer.data
        return Response(new_data, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
"""
