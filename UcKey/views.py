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
        callback_url="http://%s/login/CheckView/"% host
        Com=Common()
        data=Com.loginUrl(callback_url)
        return redirect(data['result'])



# {u'jsonrpc': u'2.0', u'id': u'1', u'result': 1125}
class CheckView(TemplateView):

    template_name="UcKey/login_index.html"

    def __init__(self):
        self.Com=Common()
        self.Parameter_missing={"error":"参数丢失"}
        self.Acquisition_failure = {"error": "获取失败"}

    def get(self,request):
        token = request.GET.get("token")
        if token is "":
            return JsonRes(json.dumps(self.Parameter_missing))

        data=self.Com.checkToken(token)
        if data['result'] == False and data == None:
            print("data=%s"%data)
            return JsonRes(json.dumps(self.Acquisition_failure))

        User_some=self.Com.getUserById(data['result'])
        Roles_some=self.Com.getRolesById(data['result'])
        print("User_some\n",User_some)
        print("Roles_some\n", Roles_some)

        return JsonRes(json.dumps(data))

