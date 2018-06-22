# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0022_auto_20180622_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='updated_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False),
        ),
    ]