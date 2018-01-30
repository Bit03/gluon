# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-30 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('dapps', '0016_auto_20180129_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dapp',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='github',
            name='readme',
            field=models.TextField(blank=True, default=''),
        ),
    ]
