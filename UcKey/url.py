#!/usr/bin/python
#coding=utf-8

from django.conf.urls import url
from django.contrib import admin

from views import login_index
urlpatterns = [
    url(r'^login_index/', login_index.as_views(),name="login_index"),

]
