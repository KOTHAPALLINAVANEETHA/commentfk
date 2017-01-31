# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170131_1413'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(default=datetime.datetime(2017, 1, 31, 14, 21, 56, 520097, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
