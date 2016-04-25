# -*- encoding: utf-8 -*-
from django.conf.urls import url
from User.views import UserPageView, SuccessLoginView, SuccessSignUpView, SuccessLogoutView
# from django.contrib.auth import
from . import views
urlpatterns = [
    url(r'^$', UserPageView.as_view(), name='user_list'),
    url(r'^success-signup', SuccessSignUpView.as_view(), name='success-signup'),
    url(r'^success-loguin', SuccessLoginView.as_view(), name='success-loguin'),
    url(r'^success-logout', SuccessLogoutView.as_view(), name='success-logout'),
    url(r'^login/$', views.authentication, name='authentication'),
    url(r'^create', views.create_data, name='create_data'),

]
