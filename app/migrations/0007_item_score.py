# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-24 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180224_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='score',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
