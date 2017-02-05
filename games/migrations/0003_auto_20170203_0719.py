# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-03 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20170203_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gamecategory',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, unique=True),
        ),
    ]
