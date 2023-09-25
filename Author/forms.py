from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import MyAuthor


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = MyAuthor
        fields = ['first_name', 'last_name', 'profile_pic','bio','address','username', 'password', ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
