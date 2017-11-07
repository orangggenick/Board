# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0004_auto_20171106_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='boxes_count',
            field=models.IntegerField(default=10, verbose_name='Колиество коробок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='end_date',
            field=models.DateField(default='2017-01-01', verbose_name='Дата окончания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='objects_in_box',
            field=models.IntegerField(default=5, verbose_name='Колиество товара в коробке'),
            preserve_default=False,
        ),
    ]
