from django import forms
from .models import User


class SignupModelForm(forms.ModelForm):
    conf_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_photo(self):
        photo = self.cleaned_data.get('photo', False)
        if photo:
            if photo.size > 500 * 1024:
                raise forms.ValidationError("Image file too large ( > 500kB )")
            return photo
        else:
            raise forms.ValidationError("Couldn't read uploaded image")

    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
            'photo': forms.FileInput()
        }
        fields = [
            'title',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'mobile_number',
            'education',
            'degree',
            'field_of_study',
            'reg_type',
            'country',
            'city',
            'postal_address',
            'password',
            'photo'
        ]


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput, label="Email", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
