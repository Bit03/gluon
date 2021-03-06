# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-29 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dapps', '0015_dapp_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dapp',
            options={'ordering': ('last_update',), 'verbose_name': 'Decentralised Applications', 'verbose_name_plural': 'Decentralised Applications'},
        ),
        migrations.AlterField(
            model_name='contractaddress',
            name='kovan',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='contractaddress',
            name='mainnet',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='contractaddress',
            name='rinkeby',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='contractaddress',
            name='ropsten',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='dapp',
            name='country_of_origin',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='dapp',
            name='etherian',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='dapp',
            name='founder',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='dapp',
            name='ico_status',
            field=model_utils.fields.StatusField(blank=True, choices=[(0, 'dummy')], default=None, max_length=100, no_check_for_status=True, null=True),
        ),
        migrations.AlterField(
            model_name='dapp',
            name='license',
            field=model_utils.fields.StatusField(blank=True, choices=[(0, 'dummy')], default=None, max_length=100, no_check_for_status=True, null=True),
        ),
        migrations.AlterField(
            model_name='dapp',
            name='status',
            field=model_utils.fields.StatusField(blank=True, choices=[(0, 'dummy')], default='demo', max_length=100, no_check_for_status=True, null=True),
        ),
        migrations.AlterField(
            model_name='dapp',
            name='vc',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='site',
            name='whitepaper',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='bitcointalk',
            field=models.URLField(blank=True, default='', max_length=255, verbose_name='BitcoinTalk'),
        ),
        migrations.AlterField(
            model_name='social',
            name='blog',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='dapp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social', to='dapps.DApp'),
        ),
        migrations.AlterField(
            model_name='social',
            name='facebook',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='gitter',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='google_plus',
            field=models.URLField(blank=True, default='', max_length=255, verbose_name='Google+'),
        ),
        migrations.AlterField(
            model_name='social',
            name='instagram',
            field=models.URLField(blank=True, default='', max_length=255, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='social',
            name='kakao',
            field=models.URLField(blank=True, default='', max_length=255, verbose_name='Kakao'),
        ),
        migrations.AlterField(
            model_name='social',
            name='linkedin',
            field=models.URLField(blank=True, default='', max_length=255, verbose_name='LinkedIn'),
        ),
        migrations.AlterField(
            model_name='social',
            name='medium',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='reddit',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='slack',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='telegram',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='twitter',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='wiki',
            field=models.URLField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='social',
            name='youtube',
            field=models.URLField(blank=True, default='', max_length=255, verbose_name='Youtube'),
        ),
    ]
