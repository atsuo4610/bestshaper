# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-31 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20170530_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brassiere',
            name='bra_started_at',
        ),
        migrations.RemoveField(
            model_name='brassiere',
            name='user',
        ),
    ]
