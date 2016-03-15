from django.contrib import admin
from cms.models import Team
from cms.forms import TeamUseradminForm
from adminsortable.admin import SortableAdmin


@admin.register(Team)
class TeamUseradmin(SortableAdmin):
    form = TeamUseradminForm

    list_display = (
        'name',
    )

    search_fields = (
        'name',
    )
