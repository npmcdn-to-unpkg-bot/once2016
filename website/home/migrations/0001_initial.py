# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 10:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('user_phone', models.CharField(max_length=32)),
                ('user_email', models.CharField(max_length=32)),
                ('submit_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(default=datetime.datetime.now)),
                ('time1', models.IntegerField(default=0)),
                ('time2', models.IntegerField(default=0)),
                ('time3', models.IntegerField(default=0)),
                ('time4', models.IntegerField(default=0)),
                ('time5', models.IntegerField(default=0)),
                ('time6', models.IntegerField(default=0)),
                ('time7', models.IntegerField(default=0)),
                ('time8', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_code', models.CharField(max_length=128)),
                ('image_name', models.CharField(max_length=128)),
            ],
        ),
    ]
