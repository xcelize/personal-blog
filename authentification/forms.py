from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email')


class LoginForm(forms.Form):

    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
