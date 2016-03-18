# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):

    name = models.CharField(
        max_length=40,
        verbose_name='Nombre del equipo',
    )

    logo = models.ImageField(
        blank=True,
        max_length=255,
        verbose_name='Fotografía',
    )

    description = models.CharField(
        max_length=400,
        blank=True,
        verbose_name="Descripción del equipo",

    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
