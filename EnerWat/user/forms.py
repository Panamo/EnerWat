from django import forms

from .models import User


class SignupModelForm(forms.ModelForm):
    conf_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_conf_password(self):
        password = self.cleaned_data.get('password', None)
        conf_password = self.cleaned_data.get('conf_password', None)
        if password and conf_password:
            if password == conf_password:
                return conf_password
            else:
                raise forms.ValidationError("Password and conf-password are not the same")
        else:
            raise forms.ValidationError("Password and conf-password is required")

    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
        ]


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, label="Username", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    next = forms.CharField(widget=forms.HiddenInput, required=False, initial=None)
