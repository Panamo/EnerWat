# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('subject', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('keyword', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
