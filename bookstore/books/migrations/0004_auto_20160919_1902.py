# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_writer_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_favorite',
        ),
        migrations.RemoveField(
            model_name='writer',
            name='is_favorite',
        ),
    ]
