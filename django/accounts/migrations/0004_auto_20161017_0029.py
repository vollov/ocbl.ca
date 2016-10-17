# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-17 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20161017_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birthday',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birth_year',
            field=models.IntegerField(default=1988, max_length=4),
        ),
    ]