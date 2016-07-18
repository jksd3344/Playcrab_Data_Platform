#!/usr/bin/python
#coding=utf-8


from django.views.generic import TemplateView,RedirectView
from django.shortcuts import redirect
from django.http import HttpResponse
from tests import Common
import json


class JsonRes(HttpResponse):
    def __init__(self,
            content={},
            status=None,
            content_type='application/json'):

        super(JsonRes, self).__init__(
            json.dumps(content),
            status=status,
            content_type=content_type)


class LoginView(RedirectView):

    def get(self,request):
        host=request.get_host()
        callback_url= "http://%s/login/CheckView/"% host
        Com=Common()
        data=Com.loginUrl(callback_url)
        return redirect(data['result'])


class CheckView(TemplateView):

    quert_string=True
    template_name="UcKey/login_index.html"

    def get(self,request):
        token = request.GET.get("token")
        Com=Common()
        data=Com.checkToken(token)
        JsonRes(json.dumps(data))

