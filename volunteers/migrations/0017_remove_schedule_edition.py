# Generated by Django 2.1.7 on 2019-02-15 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0016_auto_20190214_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='edition',
        ),
    ]
