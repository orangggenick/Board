# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-30 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0017_auto_20171130_0552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='boxes_count',
        ),
    ]
