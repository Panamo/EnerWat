from django import forms
from .models import User


class SignupModelForm(forms.ModelForm):
    class Meta:
        model = User
        widget = {'password': forms.PasswordInput()}
        exclude = []


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = User
        widget = {'password': forms.PasswordInput()}
        fields = ['username', 'password']
