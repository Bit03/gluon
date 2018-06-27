# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0031_auto_20180625_2350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commit',
            options={'ordering': ['-commit_datetime'], 'verbose_name': 'commit', 'verbose_name_plural': 'commits'},
        ),
        migrations.AlterUniqueTogether(
            name='commit',
            unique_together=set([('repos', 'hash')]),
        ),
    ]