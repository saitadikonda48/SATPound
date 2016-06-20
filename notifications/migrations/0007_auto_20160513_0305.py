# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_auto_20160512_0438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sender_content_type',
            field=models.ForeignKey(related_name=b'nofity_sender', to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_content_type',
            field=models.ForeignKey(related_name=b'notify_target', blank=True, to='contenttypes.ContentType', null=True),
        ),
    ]
