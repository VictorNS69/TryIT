# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-08 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0009_auto_20180308_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='rolelist',
            field=models.ManyToManyField(blank=True, to='volunteers.VolunteerRole'),
        ),
    ]
