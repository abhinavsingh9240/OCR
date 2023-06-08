from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import Data


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['image']  # , 'primary_lang', 'secondary_lang']


class PasswordForm(forms.Form):
    password1 = forms.CharField(max_length=63, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=63, widget=forms.PasswordInput)


class UsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]


class NameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
