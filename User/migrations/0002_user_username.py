# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user', max_length=100, unique=True, verbose_name='Nombre de usuario'),
            preserve_default=False,
        ),
    ]
