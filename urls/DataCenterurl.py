#!/usr/bin/python
#coding=utf-8

from django.conf.urls import url
from django.contrib import admin

from DataCenter.views import *
urlpatterns = [
    url(r'^Index/', DataCenter_Index.as_view(), name="Index"),
    url(r'^test/', test.as_view(), name="test"),

]
