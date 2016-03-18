from django.contrib import admin
from cms.models import Team
from cms.forms import TeamUseradminForm
from adminsortable.admin import SortableAdmin


@admin.register(Team)
class TeamUseradmin(SortableAdmin):
    form = TeamUseradminForm

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
