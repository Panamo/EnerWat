from django import forms
from .models import User


class SignupModelForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = [
            'title',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'university',
            'education',
            'degree',
            'field_of_study',
            'reg_type',
            'country',
            'city',
            'postal_address',
            'password'
        ]


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput, label="Email", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
