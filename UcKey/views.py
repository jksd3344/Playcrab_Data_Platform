#!/usr/bin/python
#coding=utf-8


from django.views.generic import TemplateView,RedirectView
from django.shortcuts import redirect
from tests import AccessApi


class LoginView(RedirectView):

    template_name='UcKey/login_index.html'

    def get(self,request):
        host=request.get_host()
        callback_url= "http://%s/userscheck/" % host
        Accpi=AccessApi("loginUrl",callback_url,'common/rpc')
        url=Accpi.post()
        print"url%s"%url
        return redirect(url['result'])
