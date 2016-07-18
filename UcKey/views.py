#!/usr/bin/python
#coding=utf-8


from django.views.generic import TemplateView,RedirectView
from django.shortcuts import redirect
from tests import Common


class LoginView(RedirectView):

    def get(self,request):
        host=request.get_host()
        callback_url= "http://%s/login/CheckView/"% host
        Com=Common()
        url=Com.loginUrl(callback_url)
        return redirect(url['result'])


class CheckView(TemplateView):

    quert_string=True
    template_name="UcKey/login_index.html"

    def get(self,request):
        token = request.GET.get("token")
        Com=Common()
