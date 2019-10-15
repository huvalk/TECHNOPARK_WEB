# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # base
    url(r'^$', views.index, name='index'),
    url(r'^ask_kuklin/', views.ask, name='ask'),
    url(r'^new/', views.question, name='question'),
]