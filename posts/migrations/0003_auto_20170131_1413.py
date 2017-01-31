# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_subscibers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='likes', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
