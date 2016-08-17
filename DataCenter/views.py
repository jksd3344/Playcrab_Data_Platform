#!/usr/bin/python
#coding=utf-8

from Tools.SomeTool import *
from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView


# Create your views here.



class DataCenter_Index(TemplateView):
    '''逻辑主页'''
    template_name="AppSome/Datacenter.html"

    @Session_vf
    def get(self,request):
        return render(request, "AppSomeShow/Datacenter.html")



class test(TemplateView):
    '''测试'''
    def post(self,request):
        username=request.POST.get("username")
        passward=request.POST.get("passward")

        print("show=",username,passward)
        return JsonRes(json.dumps({"username":username,"passward":passward}))

