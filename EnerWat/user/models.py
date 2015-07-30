from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Validators
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'.")
    # Fields
    phone_number = models.CharField(validators=[phone_regex, ], max_length=20, verbose_name='phone number',
                                    help_text="Phone number must be entered in the format: '+999999999'."
                                    )
    university = models.CharField(max_length=255, verbose_name='university')
    major = models.CharField(max_length=255, verbose_name='major')

    AbstractUser._meta.get_field_by_name('email')[0]._unique = True
    AbstractUser._meta.get_field_by_name('email')[0].blank = False


class Article(models.Model):
    writer_id = models.IntegerField()
