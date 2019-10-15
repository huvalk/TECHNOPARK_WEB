# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    # base
    url(r'^$', views.index, name='index'),
    url(r'^new/', views.new_question, name='new_question')
]