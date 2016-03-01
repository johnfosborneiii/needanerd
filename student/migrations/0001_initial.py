# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appsecurity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('userprofile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='appsecurity.UserProfile')),
                ('currentmajor', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='StudentSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.IntegerField()),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('currentmajor', models.CharField(max_length=32)),
                ('objective', models.TextField(blank=True)),
            ],
        ),
    ]
