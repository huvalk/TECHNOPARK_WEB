# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # base
    url(r'^$', views.index, name='index'),
    url(r'^hot/', views.hot, name='hot'),
    url(r'^tag/(?P<val>[A-Z a-z]*)', views.tag, name='hot'),
    url(r'^ask_kuklin/', views.ask, name='ask'),
    url(r'^new/', views.question, name='question'),
]

