# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loratemperature', '0002_remove_sensordata_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]
