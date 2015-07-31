from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Validators
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'.")
    # Fields
    title = models.CharField(max_length=255, verbose_name='title',
                             choices=[('prof', 'Prof.'), ('dr', 'Dr.'), ('mr', 'Mr.'), ('mrs', 'Mrs.')])
    phone_number = models.CharField(validators=[phone_regex, ], max_length=20, verbose_name='phone number')
    mobile_number = models.CharField(validators=[phone_regex, ], max_length=20, verbose_name='mobile number')
    education = models.CharField(max_length=255, verbose_name='education',
                                 choices=[('phd', 'PhD'), ('md', 'MD'), ('phd_can', 'PhD Candidate'),
                                          ('msc', 'MSc'), ('msc_stu', 'MSc Student'), ('bsc', 'BSc'),
                                          ('other', 'Other')])
    degree = models.CharField(max_length=255, verbose_name='degree', choices=[('prof', 'Professor'),
                                                                              ('assoc_prof', 'Associate Professor'),
                                                                              ('assist_prof', 'Assistant Professor'),
                                                                              ('instr', 'Instructor'),
                                                                              ('other', 'Other')])
    field_of_study = models.CharField(max_length=255, verbose_name='field of study')
    reg_type = models.CharField(max_length=255, verbose_name='registration type', choices=[
        ('general', 'General'), ('student', 'Student')])
    country = models.CharField(max_length=255, verbose_name='country')
    city = models.CharField(max_length=255, verbose_name='city')
    postal_address = models.TextField(verbose_name='postal address')
    photo = models.ImageField(verbose_name='photo', upload_to='users_photo')

    AbstractUser._meta.get_field_by_name('email')[0]._unique = True
    AbstractUser._meta.get_field_by_name('email')[0].blank = False


class Article(models.Model):
    writer_id = models.IntegerField()
