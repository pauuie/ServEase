from django.forms import ModelForm
from .models import Booking
#login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

class CreateAccountForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']