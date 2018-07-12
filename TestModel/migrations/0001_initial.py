# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-12 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=64)),
                ('passwd', models.CharField(max_length=64)),
                ('authority', models.CharField(max_length=64)),
                ('registTime', models.DateTimeField()),
            ],
        ),
    ]