#!/usr/bin/python
#coding=utf-8

from django.conf.urls import url
from django.contrib import admin

from UcKey.views import *
urlpatterns = [
    # url(r'^LoginView/', LoginView.as_view(),name="LoginView"),
    url(r'^some/',some.as_view(),name="some")
]
