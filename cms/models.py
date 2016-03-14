# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from adminsortable.models import SortableMixin

from django.db import models

# Create your models here.
class Team(SortableMixin):

    name = models.CharField(
        max_length=40,
        verbose_name='Nombre del equipo',
    )

    logo = models.ImageField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='Fotografía',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
