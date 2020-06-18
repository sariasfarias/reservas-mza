# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-06 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_restaurant_capacity_reserved'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReserveByHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(default=0)),
                ('currently_free', models.BooleanField(default=True)),
                ('hour', models.TimeField(default='00:00')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant')),
            ],
        ),
    ]
