# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-24 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0023_merge_20161019_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='city',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='conference',
            name='venue',
            field=models.TextField(blank=True, default=''),
        ),
    ]
