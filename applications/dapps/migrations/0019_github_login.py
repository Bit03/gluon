# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapps', '0018_auto_20180622_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='github',
            name='login',
            field=models.CharField(default='', max_length=64),
        ),
    ]
