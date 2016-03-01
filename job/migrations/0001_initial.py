# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '__first__'),
        ('employer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=3200)),
                ('skills', models.CharField(max_length=1000)),
                ('startdate', models.CharField(max_length=16)),
                ('enddate', models.CharField(max_length=16)),
                ('salary', models.CharField(max_length=16)),
                ('released', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('applicant', models.ManyToManyField(blank=True, to='student.Student')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.Employer')),
            ],
        ),
        migrations.CreateModel(
            name='JobSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobpk', models.CharField(max_length=32)),
                ('studentpk', models.CharField(blank=True, max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('applied', models.BooleanField()),
                ('employer', models.CharField(max_length=32)),
                ('employerpk', models.CharField(max_length=32)),
                ('salary', models.CharField(max_length=32)),
                ('updated_at', models.CharField(max_length=32)),
            ],
        ),
    ]
