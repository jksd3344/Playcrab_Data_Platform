#!/usr/bin/python
#coding=utf-8


import json
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse




class JsonRes(HttpResponse):
    '''httpresponse封装'''

    def __init__(self,
            content={},
            status=None,
            content_type='application/json'):

        super(JsonRes, self).__init__(
            json.dumps(content),
            status=status,
            content_type=content_type)


def Session_vf(func):
    '''
        session验证
        session过期时间:30min
        FuncSelf:self
        FuncRequest:request
    '''

    def Refunc(FuncSelf,FuncRequest):
        username=FuncRequest.session.get("username")
        print("username",username)

        '''如果没有session 则重定向到授权登陆页面'''
        if username is None:
            return redirect(reverse("UcKey:LoginView", args=[]))

        return func(FuncSelf,FuncRequest)
    return Refunc
