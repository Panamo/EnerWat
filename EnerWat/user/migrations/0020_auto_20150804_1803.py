# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20150731_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='user',
            name='education',
        ),
        migrations.RemoveField(
            model_name='user',
            name='field_of_study',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='postal_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='reg_type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='title',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address', blank=True),
        ),
    ]
