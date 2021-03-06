# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-27 02:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('game', '0003_auto_20161022_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerGameScore',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('starters', models.CharField(choices=[('Y', 'Starter'), ('S', 'Substitutes'), ('NP', 'Not Play')], default='S', max_length=2)),
                ('personal_foul', models.IntegerField(blank=True, default=0, null=True)),
                ('free_throw', models.IntegerField(default=0)),
                ('field_goal', models.IntegerField(default=0)),
                ('three_point', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='team.Player')),
            ],
            options={
                'ordering': ['player__number'],
                'db_table': 'palyer_game_score',
            },
        ),
    ]
