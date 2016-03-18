from django.contrib import admin
from cms.models import Team
from cms.models import Picture
# from cms.forms import TeamUseradminForm
from adminsortable.admin import SortableAdmin

class Pictureadmin(admin.TabularInline):
    model = Picture
    extra = 1

    fields = (
        'name',
        'image',
    )
    ordering = (
        'id',
    )
@admin.register(Team)
class TeamUseradmin(SortableAdmin):
    model = Team
    inlines = [Pictureadmin]

    list_display = (
        'name',
        'logo',
        'description',
    )

    search_fields = (
        'name',
        'logo',
        'description',
    )

    list_filter = (
        'name',
    )
    ordering = (
        'id',
    )
