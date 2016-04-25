# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models

class UserData(models.Model):

    username = models.CharField(
        unique=True,
        verbose_name='Nombre de usuario',
        max_length=100,
    )

    user_password = models.CharField(
        unique=True,
        verbose_name='Password de usuario',
        max_length=100,
    )

class UserDataComplete(models.Model):

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'document_type',
        'document_number',
    ]

    DOCUMENT_CHOICES = (
        (10, 'Cedula de ciudadanía'),
        (20, 'Cedula de extranjería'),
        (30, 'Pasaporte'),
    )

    GENRE_CHOICES = (
        (10, 'Masculino'),
        (20, 'Femenino'),
        (30, 'Otro'),
    )

    email = models.EmailField(
        unique=True,
        verbose_name='Correo electrónico',
    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='Nombres',
    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='Apellidos',
    )

    document_type = models.PositiveSmallIntegerField(
        choices=DOCUMENT_CHOICES,
        verbose_name='Tipo de documento',
    )

    document_number = models.CharField(
        max_length=64,
        verbose_name='Número de documento',
    )

    document_expedition = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='Lugar de expedición',
    )

    nationality = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='Nacionalidad',
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Fecha de nacimiento',
    )

    department = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='Departamento',
    )

    city = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='Ciudad',
    )

    address = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='Dirección',
    )

    mobile_phone = models.CharField(
        blank=True,
        null=True,
        max_length=64,
        verbose_name='Teléfono Celular',
    )

    genre = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        choices=GENRE_CHOICES,
        verbose_name='Genero',
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de registro',
    )


    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        unique_together = ('document_type', 'document_number')
        ordering = ('first_name', 'last_name')
