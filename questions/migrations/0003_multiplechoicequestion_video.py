# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0016_auto_20160513_1833'),
        ('questions', '0002_auto_20160519_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoicequestion',
            name='video',
            field=models.ForeignKey(default=1, to='videos.Video'),
            preserve_default=True,
        ),
    ]
