# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0009_auto_20180215_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositorystats',
            name='date',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]
