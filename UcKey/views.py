#!/usr/bin/python
#coding=utf-8


import json
from apps import Common
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView,RedirectView



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
        callback_url="http://%s/login/CheckView/"% host
        Com=Common()
        data=Com.loginUrl(callback_url)
        return redirect(data['result'])


# {u'jsonrpc': u'2.0', u'id': u'1', u'result': 1125}
class CheckView(TemplateView):

    def __init__(self):
        self.Com=Common()
        self.Parameter_missing={"error":"Token_Parameter_missing"}
        self.Token_failure = {"error": "CheckToken_Acquisition_failure"}
        self.User_failure = {"error": "GetUser_Acquisition_failure"}

    def get(self,request):
        token = request.GET.get("token")
        if token is "":
            return JsonRes(json.dumps(self.Parameter_missing))

        data=self.Com.CheckToken(token)
        if data['result'] == False and data == None:
            print("data=%s"%data)
            return JsonRes(json.dumps(self.Acquisition_failure))

        User_some=self.Com.getUserById(data['result'])
        Roles_some=self.Com.getRolesById(data['result'])
        if User_some.get("result") is None and Roles_some.get("result") is None:
            print("User_some\n",User_some)
            print("Roles_some\n", Roles_some)
            return JsonRes(json.dumps(self.User_failure))

        request.session["username"]=(User_some.get("result","")).get("name","")

        return redirect(reverse("UcKey:Index", args=[]))

def Session_vf(func):
    def Refunc(*args, **kw):
        print("sss=",args,kw)
        return func
    return Refunc


class Index(TemplateView):
    template_name="UcKey/login_index.html"

    @Session_vf
    def Re_some(self,request):
        return 1

    def get_context_data(self,**kwargs):
        context=super(Index,self).get_context_data(**kwargs)
        context["some"]=self.Re_some()
        return context





