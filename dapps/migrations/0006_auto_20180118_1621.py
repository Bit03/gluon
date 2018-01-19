# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-18 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dapps', '0005_auto_20180118_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainnet', models.CharField(max_length=128, null=True)),
                ('ropsten', models.CharField(max_length=128, null=True)),
                ('kovan', models.CharField(max_length=128, null=True)),
                ('rinkeby', models.CharField(max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Contract Address',
                'verbose_name_plural': 'Contract Address',
            },
        ),
        migrations.AddField(
            model_name='dapp',
            name='last_update',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='dapp',
            name='submitted',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contractaddress',
            name='dapp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='dapps.DApp'),
        ),
    ]
