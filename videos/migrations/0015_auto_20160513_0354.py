# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_auto_20160511_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ForeignKey(default=1, to='videos.Category'),
        ),
        migrations.AlterField(
            model_name='video',
            name='share_message',
            field=models.TextField(default=b'Check out this awesome video.'),
        ),
    ]
