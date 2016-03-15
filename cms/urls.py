# -*- encoding: utf-8 -*-
from django.conf.urls import url
from cms.views import TeamListView


urlpatterns = [
    url(r'^teams/$',TeamListView.as_view(),name='team_list'),
]
