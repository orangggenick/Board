# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 16:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0028_auto_20171205_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='public_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 5, 16, 23, 5, 11671), verbose_name='Дата публикации'),
        ),
    ]
