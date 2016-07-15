#!/usr/bin/python
#coding=utf-8


from django.views.generic import TemplateView,RedirectView
from django.shortcuts import redirect
from tests import AccessApi


class LoginView(RedirectView):

    def get(self,request):
        host=request.get_host()
        callback_url= "http://%s/userscheck/" % host
        Accpi=AccessApi("loginUrl",callback_url,'common/rpc')
        url=Accpi.post()
        print"url%s"%url
        print"callback_url%s" % callback_url
        return redirect(url['result'])

