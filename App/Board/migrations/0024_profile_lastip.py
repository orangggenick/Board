# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0023_profile_lastlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lastIP',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='Последний IP входа'),
        ),
    ]