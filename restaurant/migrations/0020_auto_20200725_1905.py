# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-07-25 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_auto_20200710_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
