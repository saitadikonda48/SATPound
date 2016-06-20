# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_openquestion_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplechoicequestion',
            name='video',
            field=models.ForeignKey(to='videos.Video'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='openquestion',
            name='video',
            field=models.ForeignKey(to='videos.Video'),
            preserve_default=True,
        ),
    ]
