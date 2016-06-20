# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0016_auto_20160513_1833'),
        ('questions', '0003_multiplechoicequestion_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='openquestion',
            name='video',
            field=models.ForeignKey(default=True, to='videos.Video'),
            preserve_default=True,
        ),
    ]
