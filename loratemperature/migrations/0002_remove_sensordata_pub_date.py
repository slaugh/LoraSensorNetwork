# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 03:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loratemperature', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensordata',
            name='pub_date',
        ),
    ]
