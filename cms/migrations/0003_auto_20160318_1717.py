# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20160318_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ['name'], 'verbose_name': 'Imagen', 'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['name'], 'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AddField(
            model_name='team',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(10, 'A'), (20, 'B')], default=20, verbose_name='Categor\xeda de la instituci\xf3n'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nombre del equipo'),
        ),
    ]