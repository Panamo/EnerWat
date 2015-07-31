# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20150730_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='major',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=datetime.datetime(2015, 7, 31, 7, 41, 48, 715425, tzinfo=utc), verbose_name='city', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default=datetime.datetime(2015, 7, 31, 7, 41, 56, 147557, tzinfo=utc), verbose_name='country', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='degree',
            field=models.CharField(default=datetime.datetime(2015, 7, 31, 7, 42, 0, 40877, tzinfo=utc), verbose_name='degree', max_length=255, choices=[('prof', 'Professor'), ('assoc_prof', 'Associate Professor'), ('assist_prof', 'Assistant Professor'), ('instr', 'Instructor'), ('other', 'Other')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.CharField(default=datetime.datetime(2015, 7, 31, 7, 42, 10, 881785, tzinfo=utc), verbose_name='education', max_length=255, choices=[('phd', 'PhD'), ('md', 'MD'), ('phd_can', 'PhD Candidate'), ('msc', 'MSc'), ('msc_stu', 'MSc Student'), ('bsc', 'BSc'), ('other', 'Other')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='field_of_study',
            field=models.CharField(default=datetime.datetime(2015, 7, 31, 7, 42, 13, 926461, tzinfo=utc), verbose_name='field of study', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(verbose_name='mobile number', default=datetime.datetime(2015, 7, 31, 7, 42, 17, 27699, tzinfo=utc), validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")], max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='postal_address',
            field=models.TextField(default=1, verbose_name='postal address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='reg_type',
            field=models.CharField(default=datetime.datetime(2015, 7, 31, 7, 42, 26, 257355, tzinfo=utc), verbose_name='registration type', max_length=255, choices=[('general', 'General'), ('student', 'Student')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(default=1, verbose_name='title', max_length=255, choices=[('prof', 'Prof.'), ('dr', 'Dr.'), ('mr', 'Mr.'), ('mrs', 'Mrs.')]),
            preserve_default=False,
        ),
    ]
