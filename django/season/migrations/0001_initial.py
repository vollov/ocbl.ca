# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-04 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0003_auto_20161129_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('school', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
            options={
                'ordering': ['-start_date'],
                'db_table': 'season',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('season', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='season.Season')),
            ],
            options={
                'ordering': ['start_time'],
                'db_table': 'session',
            },
        ),
    ]