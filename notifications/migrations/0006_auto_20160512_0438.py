# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_remove_notification_unread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='target_object_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
