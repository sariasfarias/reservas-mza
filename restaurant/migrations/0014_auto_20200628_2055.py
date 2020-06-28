# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-28 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_auto_20200627_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='columns',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='rows',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='tables',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='closed',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='open',
            field=models.TimeField(blank=True, null=True),
        ),
    ]