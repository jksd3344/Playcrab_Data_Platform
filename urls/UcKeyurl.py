#!/usr/bin/python
#coding=utf-8

from django.conf.urls import url
from django.contrib import admin

from UcKey.views import LoginView
urlpatterns = [
    url(r'^LoginView/', LoginView.as_view(),name="LoginView"),

]
