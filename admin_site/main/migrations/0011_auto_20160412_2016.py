# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20160412_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verify_type',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
    ]
