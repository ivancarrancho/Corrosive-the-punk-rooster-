# -*- encoding: utf-8 -*-
from django.conf.urls import url
from User.views import UserPageView
from django.views.generic import TemplateView

urlpatterns = [
    url(
        r'^$',
        UserPageView.as_view(),
        name='user_list'
    ),
    url(r'^succes', TemplateView.as_view()),
]
