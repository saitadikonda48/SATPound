# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='twitter_handle',
            field=models.CharField(max_length=320, null=True, verbose_name=b'Twitter handle', blank=True),
        ),
    ]
