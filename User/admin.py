# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group

from User.models import UserDataComplete


admin.site.unregister(Group)

@admin.register(UserDataComplete)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'document_number',
    )

    search_fields = ('first_name', 'last_name', 'email', 'document_number')

    add_fieldsets = (
        ('Información básica', {
            'fields': (
                'first_name',
                'last_name',
                'document_type',
                'document_number',
                ),
            }),
        # ('Información de acceso', {
        #     'fields': (
        #         'email',
        #         'password1',
        #         'password2',
        #         ),
        #     }),
        )

    fieldsets = (
        ('Información de acceso', {
            'fields': (
                'email',
                # 'password',
                ),
            }),
        ('Información básica', {
            'fields': (
                'first_name',
                'last_name',
                'document_type',
                'document_number',
                'document_expedition',
                ),
            }),
        ('Información personal', {
            'fields': (
                'genre',
                'nationality',
                'birth_date',
                'department',
                'city',
                'address',
                'mobile_phone',
            ),
        })
    )

    ordering = ('first_name', 'last_name')

    def get_actions(self, request):
        actions = super(CustomUserAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = super(CustomUserAdmin, self).get_readonly_fields(
            request, obj
        )
        return read_only_fields + ('last_login', 'date_joined')

    def has_delete_permission(self, request, obj=None):
        return False
