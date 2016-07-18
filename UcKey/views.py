#!/usr/bin/python
#coding=utf-8


import json
from apps import Common
from Tools.tool import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView,RedirectView




class LoginView(RedirectView):
    '''授权登陆'''

    def get(self,request):
        host=request.get_host()
        callback_url="http://%s/login/CheckView/"% host

        Com=Common()
        data=Com.loginUrl(callback_url)
        return redirect(data['result'])



class CheckView(TemplateView):
    '''授权登录验证'''

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
            return JsonRes(json.dumps(self.Acquisition_failure))


        User_some=self.Com.getUserById(data['result'])
        Roles_some=self.Com.getRolesById(data['result'])
        if User_some.get("result") is None and Roles_some.get("result") is None:
            return JsonRes(json.dumps(self.User_failure))


        request.session["username"]=(User_some.get("result","")).get("name","")
        return redirect(reverse("UcKey:Index", args=[]))



class Index(TemplateView):
    '''逻辑主页'''
    template_name="UcKey/login_index.html"

    @Session_vf
    def get(self,request):
        return render(request,"UcKey/login_index.html")








class text(TemplateView):
    template_name = "UcKey/login_index.html"






























