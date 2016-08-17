#!/usr/bin/python
#coding=utf-8


from __future__ import unicode_literals
from Tools.SomeTool import Send_mail
import pymysql
import datetime
from _models.models import LoginMsg
db_show = pymysql.connect(host="123.57.226.182",user="root",passwd="Jksd3344",db="Shake",charset="utf8")
db = db_show.cursor()

# Create your models here.



