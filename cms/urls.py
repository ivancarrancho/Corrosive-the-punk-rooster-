# -*- encoding: utf-8 -*-
from django.conf.urls import url
from cms.views import TeamListView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^teams/$',TeamListView.as_view(),name='team_list'),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
