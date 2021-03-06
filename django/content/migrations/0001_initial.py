# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-19 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('code', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('locale', models.CharField(choices=[('en', 'English'), ('zh', 'Chinese')], default=b'zh', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=64, primary_key=True, serialize=False, verbose_name='Activation key')),
                ('name', models.CharField(blank=True, max_length=32, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Page'),
        ),
    ]
