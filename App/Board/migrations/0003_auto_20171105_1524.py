# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('Board', '0002_auto_20171104_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ID автора')),
            ],
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='city',
            field=models.CharField(default='Не выбрано', max_length=20, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], keep_meta=True, quality=0, size=[360, 360], upload_to='', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Не выбрано', max_length=20, verbose_name='Город'),
        ),
    ]
