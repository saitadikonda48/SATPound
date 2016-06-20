# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_auto_20160511_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taggeditem',
            old_name='tag',
            new_name='tags',
        ),
    ]
