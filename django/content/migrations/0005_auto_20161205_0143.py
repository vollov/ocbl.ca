# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-05 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20161204_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='locale',
            field=models.CharField(choices=[('en', 'English'), ('zh', 'Chinese')], default=b'zh', max_length=2),
        ),
    ]
