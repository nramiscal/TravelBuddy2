# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-27 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
        ('trip_app', '0003_auto_20171025_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='join',
            name='user',
        ),
        migrations.AddField(
            model_name='trip',
            name='joiners',
            field=models.ManyToManyField(related_name='joins', to='user_app.User'),
        ),
        migrations.DeleteModel(
            name='Join',
        ),
    ]
