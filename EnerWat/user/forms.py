from django import forms
from .models import User


class SignupModelForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'first_name': "First Name",
            'last_name': "Last Name",
            'email': "Email",
            'phone_number': "Phone Number",
            'university': "University",
            'major': "Major",
            'password': "Password"
        }
        exclude = []


class LoginModelForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'email': "Email",
            'password': "Password"
        }
        fields = ['email', 'password']
