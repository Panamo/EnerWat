# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_remove_user_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(verbose_name='photo', upload_to='users_photo', default=datetime.datetime(2015, 7, 31, 16, 39, 49, 114887, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
