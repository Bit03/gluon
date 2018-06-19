# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 06:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=64)),
                ('platform', models.CharField(max_length=64)),
                ('symbol', models.CharField(blank=True, max_length=64, null=True)),
                ('description', models.TextField(blank=True, default='')),
                ('description_cn', models.TextField(blank=True, default='')),
                ('country_of_origin', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'verbose_name': 'Decentralised Applications',
                'verbose_name_plural': 'Decentralised Applications',
            },
        ),
        migrations.CreateModel(
            name='GitHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255)),
                ('readme', models.TextField()),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('dapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='github', to='dapps.DApp')),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('dapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logo', to='dapps.DApp')),
            ],
            options={
                'verbose_name': 'logo',
                'verbose_name_plural': 'logo',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255)),
                ('whitepaper', models.URLField(max_length=255)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('dapp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='site', to='dapps.DApp')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Site',
            },
        ),
    ]