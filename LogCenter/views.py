#!/usr/bin/python
#coding=utf-8

from Tools.SomeTool import *
from django.shortcuts import render
from django.views.generic import TemplateView,RedirectView
from models import LogCenter
Lc=LogCenter()

# Create your views here.



class LogCenter_index(TemplateView):
    '''日志中心逻辑主页'''
    template_name="AppSome/LogCenter.html"

    @Session_vf_PageId
    def get(self,request,PageId):

        Lc.FindLogCenter_init(5)
        data = Lc.FindLogCenter_ReData(PageId)

        Lc.FindLogCenter_RePage_init(3)
        PageData=Lc.FindLogCenter_RePage(PageId)

        Re_data={
            "L_data":data,
            "PageData": PageData,
            "PageId":int(PageId),
            "TotalPage":Lc.TotalPage
        }

        return render(request,"AppSomeShow/LogCenter.html",Re_data)














