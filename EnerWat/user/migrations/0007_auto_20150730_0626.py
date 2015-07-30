# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20150730_0258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='email', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(verbose_name='first name', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(verbose_name='last name', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='major',
            field=models.CharField(verbose_name='major', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(verbose_name='phone number', max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.CharField(verbose_name='university', max_length=255),
        ),
    ]
