# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20150731_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='university',
        ),
    ]
