# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0016_auto_20160513_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('choiceA', models.CharField(max_length=350)),
                ('choiceB', models.CharField(max_length=350)),
                ('choiceC', models.CharField(max_length=350)),
                ('choiceD', models.CharField(max_length=350)),
                ('correctAnswer', models.CharField(max_length=1)),
                ('answerExplanation', models.TextField()),
                ('help', models.TextField()),
                ('video', models.ForeignKey(blank=True, to='videos.Video', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpenQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('answer', models.CharField(max_length=10)),
                ('help', models.TextField()),
                ('video', models.ForeignKey(blank=True, to='videos.Video', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
