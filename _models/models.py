# !/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models
import datetime

class LoginMsg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)  # uid
    name = models.CharField(unique=True,max_length=32) #姓名
    account = models.CharField(unique=True, max_length=32) #账户名
    phone = models.CharField(unique=True, max_length=16) #手机号
    number = models.IntegerField(blank=True, null=True) #工号
    sex = models.CharField(unique=True, max_length=4) #性别
    email = models.CharField(unique=True, max_length=32) #邮箱
    department_id = models.IntegerField(blank=True, null=True) #部门号
    role_name = models.CharField(unique=True, max_length=32) #角色
    createtime = models.DateTimeField(default=datetime.datetime.now) #创建时间
    killtime = models.DateTimeField(default=datetime.datetime.now) #删除时间

    class Meta:
        managed = False
        db_table = "LoginMsg"






