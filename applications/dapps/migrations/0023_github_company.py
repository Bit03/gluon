# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapps', '0022_github_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='github',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
