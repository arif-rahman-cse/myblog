from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Our Custom registration form inherit from UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # Model I want to interact
        model = User
        # Filed i want to show according to serial
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
