from django.contrib import admin
from cms.models import Team
from cms.forms import TeamUseradminForm
from adminsortable.admin import SortableAdmin


@admin.register(Team)
class TeamUseradmin(SortableAdmin):
    form = TeamUseradminForm

    list_display = (
        'name',
        'category',
        'is_active',
    )

    list_filter = (
        'category',
        'is_active',
    )

    search_fields = (
        'name',
    )
