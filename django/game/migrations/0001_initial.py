# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('host_score', models.IntegerField(blank=True, default=0, null=True)),
                ('guest_score', models.IntegerField(blank=True, default=0, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('finished', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='team.Team')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='team.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Recorder',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='master_referee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Referee'),
        ),
        migrations.AddField(
            model_name='game',
            name='recorder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.Recorder'),
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Season'),
        ),
        migrations.AddField(
            model_name='game',
            name='secondary_referee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='game.Referee'),
        ),
        migrations.AddField(
            model_name='game',
            name='timer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.Timer'),
        ),
    ]
