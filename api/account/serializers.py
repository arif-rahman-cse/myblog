from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# User registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label='Password')
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, label='Confirm Password')
    email = serializers.EmailField(label='Email Address')
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'token']

        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    # Validate User Email
    def validate(self, value):
        data = self.get_initial()
        email = data.get('email')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError('The user has already registered with this email')
        return value

    # Validate Password Filed
    def validate_password(self, value):
        data = self.get_initial()
        password = data.get('password')
        con_password = data.get('password2')
        # con_password = value
        if password != con_password:
            raise ValidationError("Password must match.")
        return value

    # Override Create function to create new user
    def create(self, validated_data):
        print(validated_data)  # Printing validate data dictionary
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        # token = Token.objects.get(user=)
        user_obj = User(
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj


# User registration Serializer
class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token', ]

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, value):
        print("***************validating*******************")
        data = self.get_initial()
        # user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required to login.")
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        print(user, "-------------*********************")
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                print("wrong pwd", "**************************************")
                raise ValidationError("Incorrect credentials! Please Try again!")
        data["token"] = Token.objects.get(user=user_obj).key

        return data

    # Validate User Email


"""
    def validate(self, value):
        user_obj = None
        data = self.get_initial()
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password')
        if not email and not username:
            raise ValidationError('username and email is required to login!')
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('This username/email is not  valid!')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect credentials please try again!')
        data['token'] = 'some random token'

        return value
"""
