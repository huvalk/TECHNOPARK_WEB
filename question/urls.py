# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # base
    url(r'^$', views.index, name='index'),
    url(r'^hot/', views.hot, name='hot'),
    url(r'^tag/(?P<t>[A-Z a-z]*)', views.tag, name='tag'),
    url(r'^ask/', views.ask, name='ask'),
    url(r'^question/(?P<q>[1-9]*)', views.question, name='question'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
]

