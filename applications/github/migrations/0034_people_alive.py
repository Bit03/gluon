# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0033_repository_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='alive',
            field=models.BooleanField(default=True),
        ),
    ]
