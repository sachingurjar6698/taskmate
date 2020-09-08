from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField()
    First_Name = forms.CharField()
    Last_Name = forms.CharField()

    class Meta:
        model = User 
        fields = ['First_Name','Last_Name','username', 'email', 'password1', 'password2']
