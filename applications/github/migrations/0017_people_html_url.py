# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0016_auto_20180620_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='html_url',
            field=models.URLField(default='', max_length=255,),
        ),
    ]