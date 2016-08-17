#!/usr/bin/python
#coding=utf-8

from __future__ import unicode_literals
import pymysql
from _models.models import LoginMsg
from Tools.ShowPage import PagePaging
db_show = pymysql.connect(host="123.57.226.182",user="root",passwd="Jksd3344",db="Shake",charset="utf8")
db = db_show.cursor()

# Create your models here.


class LogCenter(object):

    def __init__(self):
        self.Page=None
        self.TotalPage=0

    def FindLogCenter_init(self,PageNu):
        '''

        :param PageNu:每页条数
        '''
        count= LoginMsg.objects.all().count()
        self.Page=PagePaging(count,PageNu)


    def FindLogCenter_ReData(self,PageId):
        '''

        :param PageId:页码
        :return: 页码对应数据
        :return: 总页数
        '''
        PageData = []
        self.TotalPage = self.Page.TotalPage()

        self.TotalPage = self.Page.Judge(self.TotalPage)
        datapage = self.Page.Re_page(PageId)
        data = LoginMsg.objects.all().order_by('-id').values()[datapage.Start:datapage.End]


        for i in range(self.TotalPage):
            PageData.append(i+1)

        return {"TotalPage":PageData,"data":data}


    def FindLogCenter_RePage_init(self,ExPage_num):
        '''

        页码初始化
        :param ExPage_num: 展示页码数量
        :return:
        '''
        self.Page.Re_Judge(ExPage_num,self.TotalPage)


    def FindLogCenter_RePage(self,PageId):
        '''

        返回指定列表
        :param PageId:页码
        :return:
        '''
        data=[]
        PageData=self.Page.Re_page_num(PageId)

        for i in range(PageData.Start_n,PageData.End_n):
            data.append(i)

        return data





