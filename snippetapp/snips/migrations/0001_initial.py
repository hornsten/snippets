# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('language', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('snip', models.CharField(max_length=300)),
            ],
        ),
    ]
