# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0015_auto_20180619_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='type',
        ),
        migrations.AddField(
            model_name='people',
            name='type',
            field=models.IntegerField(choices=[(0, 'user'), (1, 'organization')], default=0),
        ),
    ]
