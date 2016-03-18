# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from adminsortable.models import SortableMixin


class Team(SortableMixin):

    name = models.CharField(
        blank=True,
        max_length=40,
        verbose_name='Nombre del equipo',
    )

    CATEGORY_CHOICES = (
        (10, 'A'),
        (20, 'B'),
    )

    category = models.PositiveSmallIntegerField(
        choices=CATEGORY_CHOICES,
        verbose_name='Categoría de la institución',
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
        ordering = ['category']
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'


# Create your models here.
class Picture(models.Model):

    name = models.CharField(
        blank=True,
        max_length=255,
        verbose_name='Nombre del equipo',
    )

    image = models.ImageField(
        blank=True,
        max_length=255,
        verbose_name="Imagenes",
    )

    team = models.ForeignKey(
        Team,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
