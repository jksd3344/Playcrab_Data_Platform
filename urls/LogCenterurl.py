#!/usr/bin/python
#coding=utf-8

from django.conf.urls import url
from django.contrib import admin

from LogCenter.views import *
urlpatterns = [
    url(r'^Index/(\d+)/$', LogCenter_index.as_view(), name="Index"),
]
