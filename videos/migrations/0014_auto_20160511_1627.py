# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0013_auto_20160511_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taggeditem',
            old_name='tags',
            new_name='tag',
        ),
    ]
