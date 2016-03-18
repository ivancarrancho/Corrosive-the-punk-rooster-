# -*- encoding: utf-8 -*-
from cms.models import Team
from django.views.generic import ListView
# Create your views here.
#
#
class TeamListView(ListView):
    model = Team

    def get_query_set(self):
        return Team.objects.all()
