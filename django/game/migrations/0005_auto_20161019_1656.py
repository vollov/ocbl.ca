# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-19 20:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20161019_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='referee',
        ),
        migrations.AddField(
            model_name='game',
            name='master_referee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Referee'),
        ),
        migrations.AddField(
            model_name='game',
            name='secondary_referee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Referee'),
        ),
    ]
