# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoicequestion',
            name='video',
        ),
        migrations.RemoveField(
            model_name='openquestion',
            name='video',
        ),
    ]
