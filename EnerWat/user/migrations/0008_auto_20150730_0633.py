# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('user', '0007_auto_20150730_0626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'users', 'verbose_name': 'user'},
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', verbose_name='groups', related_query_name='user', blank=True, related_name='user_set'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', to='auth.Permission', verbose_name='user permissions', related_query_name='user', blank=True, related_name='user_set'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', default=datetime.datetime(2015, 7, 30, 6, 33, 27, 985205, tzinfo=utc), validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='last name', blank=True),
        ),
    ]
