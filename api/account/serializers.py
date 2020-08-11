from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


# User registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label='Password')
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, label='Confirm Password')
    email = serializers.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

        extra_kwargs = {
            'password': {'write_only': True},
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
        con_password = value
        if password != con_password:
            raise ValidationError("Password must match.")
        return value

    # Override Create function to create new user
    def create(self, validated_data):
        print(validated_data)  # Printing validate data dictionary
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
