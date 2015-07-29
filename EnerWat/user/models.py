from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class User(models.Model):
    # Validators
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # Fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(validators=[phone_regex, ], max_length=20)
    university = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=25)


class Article(models.Model):
    writer_id = models.IntegerField()
