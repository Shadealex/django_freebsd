# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 17:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_statistic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statistic',
            options={'ordering': ['name'], 'verbose_name': 'Статистика', 'verbose_name_plural': 'Статистика'},
        ),
    ]
