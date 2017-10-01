# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('society', '0003_delete_soclist'),
    ]

    operations = [
        migrations.CreateModel(
            name='soclist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('genre', models.CharField(max_length=50)),
                ('typ', models.CharField(max_length=50)),
                ('logo', models.CharField(max_length=250)),
                ('desc', models.TextField(max_length=500)),
            ],
        ),
    ]
