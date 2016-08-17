#!/usr/bin/python
#coding=utf-8


import json
from Tools.LoginApin import Common
from Tools.SomeTool import *
from model import Pmsg
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView,RedirectView
PMS=Pmsg()



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
        self.role_name=""



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

        self.Save_some(User_some,Roles_some)

        request.session["uid"]=User_some.get("result","").get("id")
        return redirect(reverse("DataCenter:Index", args=[]))



    def Send_some_mail(self):
        Sm=Send_mail("jksd517@163.com","1234liuxin",['jiayuguang@qq.com'])
        msg=Sm.Re_msg("首次登陆系统,您的所有操作已经被记录在案,感谢您的使用....","数据中心","系统给你打了声招呼")
        Sm.Send(msg)
        Sm.Quit()



    def Save_some(self,User_some,Roles_some):
        User_some = User_some.get("result")
        Roles_some = Roles_some.get("result")
        for i in Roles_some:
            self.role_name += (i.get("en_name") + ",")

        data = {
            "uid": User_some.get("id"),
            "name": User_some.get("name"),
            "account": User_some.get("account"),
            "phone": User_some.get("phone"),
            "number": User_some.get("number"),
            "sex": User_some.get("sex"),
            "email": User_some.get("email"),
            "department_id": User_some.get("department_id"),
            "role_name": self.role_name,
        }
        PMS.SaveLoginMsg(data)
































