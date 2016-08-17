#!/usr/bin/python
#coding=utf-8



import math


class PagePaging(object):
    '''翻页'''

    def __init__(self,TotalMsg,DateNu):
        '''

        :param TotalMsg:总条数
        :param DateNu:每页显示条数
        :param LineNu: 页码间隔数
        '''
        self.TotalMsg=TotalMsg
        self.DateNu=DateNu
        self.data={}
        self.Page={}



    def TotalPage(self):
        '''

        :return:计算总页数
        '''
        if self.DateNu>=self.TotalMsg:
            return 1
        return int(math.floor(self.TotalMsg/float(self.DateNu)))



    def Judge(self,TotalPage):
        '''

        初始化数据
        :param TotalPage:总页数
        :return: 返回初始化数据
        '''
        if TotalPage==1:
            self.data[1]=Page(PageNum=1,Start=0,End=self.TotalMsg)
            return self.data
        else:
            for i in range(TotalPage):
                if i is 0:
                    self.data[i+1]=Page(PageNum=i+1,Start=i,End=i+self.DateNu)
                else:
                    self.data[i+1]=Page(PageNum=i+1,Start=self.data[i].End,End=self.data[i].End+self.DateNu)
            if self.TotalMsg%self.DateNu!=0:
                self.data[TotalPage+1]=Page(PageNum=TotalPage+1,Start=self.data[TotalPage].End,End=self.TotalMsg)
                TotalPage=TotalPage+1
            return TotalPage



    def Re_page(self,Page_num):
        '''

        :param Page_num:传入页码
        :return:  返回数据开始结束位置
        '''

        Page_num=int(Page_num)
        if Page_num in self.data.keys():
            return self.data[Page_num]
        else:
            return self.data[1]



    def Re_Judge(self,ExPage_num,TotalPage):
        '''

        :param ExPage_num: 传入想要展示页码数量
        :param TotalPage: 总页数
        :return: 返回展示页码列表
        '''

        TotalPage = int(TotalPage)
        ExPage_num = int(ExPage_num)

        if TotalPage==1:
            self.Page[1]=PageNumber(1,1,TotalPage)

        elif TotalPage<=ExPage_num:
            for i in range(TotalPage+1):
                i=i+1
                self.Page[i] = PageNumber(i, 1, TotalPage)
        else:
            tp=range(TotalPage)
            tp.reverse()
            for i in tp:
                i=i+1
                if i is 1:
                    self.Page[1] = PageNumber(i, 1, i + ExPage_num)
                elif i+ExPage_num-1 > TotalPage:
                    self.Page[i]=PageNumber(i,len(tp)-ExPage_num+1,len(tp)+1)
                else:
                    self.Page[i] = PageNumber(i, i-1, i + ExPage_num-1)
        return self.Page



    def Re_page_num(self,Page_num):
        '''

        :param Page_num:页码
        :return: 翻页列表
        '''
        Page_num=int(Page_num)

        if Page_num in self.Page.keys():
            return self.Page[Page_num]
        else:
            return self.Page[1]




class PageNumber(object):
    def __init__(self,PageNum,Start,End):
        '''

        返回页码位置
        :param PageNum:页码
        :param Start: 开始位置
        :param End: 结束位置
        '''

        self._PageNum=PageNum
        self._Start=Start
        self._End=End

    @property
    def PageNum_n(self):
        return self._PageNum

    @property
    def Start_n(self):
        return self._Start

    @property
    def End_n(self):
        return self._End





class Page(object):
    def __init__(self,PageNum,Start,End):
        '''

        返回数据位置
        :param PageNum:  页码
        :param Start:    开始位置
        :param End:      结束位置
        :param NextPage: 下一页
        :param PrevPage: 上一页
        '''
        self._PageNum=PageNum
        self._Start=Start
        self._End=End
        self._NextPage=Start+1
        self._PrevPage=End-1


    @property
    def PageNum(self):
        return self._PageNum
    @property
    def Start(self):
        return self._Start
    @property
    def End(self):
        return self._End
    @property
    def NextPage(self):
        return self._NextPage
    @property
    def PrevPage(self):
        return self._PrevPage


