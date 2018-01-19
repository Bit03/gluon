# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('dapps', '0002_auto_20180118_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reddit', models.URLField(default='', max_length=255)),
                ('slack', models.URLField(default='', max_length=255)),
                ('gitter', models.URLField(default='', max_length=255)),
                ('blog', models.URLField(default='', max_length=255)),
                ('medium', models.URLField(default='', max_length=255)),
                ('wiki', models.URLField(default='', max_length=255)),
                ('twitter', models.URLField(default='', max_length=255)),
                ('facebook', models.URLField(default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='dapp',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='dapp',
            name='vc',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='dapp',
            name='country_of_origin',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='social',
            name='dapp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='socail', to='dapps.DApp'),
        ),
    ]
