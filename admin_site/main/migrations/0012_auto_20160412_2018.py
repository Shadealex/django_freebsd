# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20160412_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.TextField(max_length=100, verbose_name='Имя сервера'),
        ),
    ]
