# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160917_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
