#!/usr/bin/python
#coding=utf-8


import json
import smtplib
import paramiko
import logging
from email.header import Header
from email.mime.text import MIMEText
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse




class JsonRes(HttpResponse):
    '''httpresponse封装'''

    def __init__(self,
            content={},
            status=None,
            content_type='application/json'):

        super(JsonRes, self).__init__(
            json.dumps(content),
            status=status,
            content_type=content_type)



def Session_vf(func):
    '''
        session验证,两参
        session过期时间:30min
        FuncSelf:self
        FuncRequest:request
    '''

    def Refunc(FuncSelf,FuncRequest):

        uid=FuncRequest.session.get("uid")
        print("uid",uid)

        '''如果没有session 则重定向到授权登陆页面'''
        if uid is None:
            return redirect(reverse("UcKey:LoginView", args=[]))

        return func(FuncSelf,FuncRequest)
    return Refunc



def Session_vf_PageId(func):
    '''
        session验证,三参

        session过期时间:30min
        FuncSelf:self
        FuncRequest:request
    '''

    def Refunc(FuncSelf,FuncRequest,FuncPageId):

        uid=FuncRequest.session.get("uid")
        print("uid",uid)

        '''如果没有session 则重定向到授权登陆页面'''
        if uid is None:
            return redirect(reverse("UcKey:LoginView", args=[]))

        return func(FuncSelf,FuncRequest,FuncPageId)
    return Refunc




class Send_mail(object):
    '''发送邮件'''

    def __init__(self,sender,passward,receivers):
        '''

        :param sender: 发送者
        :param passward: 发送者密码
        :param receivers: 接收者
        '''
        self.sender=sender
        self.password=passward
        self.receivers=receivers

        self.smtpObj=None


    def Re_msg(self,ShowText,Name,Header_show):
        '''

        :param ShowText: 发送内容
        :param Name: 发送者
        :param Header_show: 发送文件抬头
        :return:
        '''
        message = MIMEText('%s'%(ShowText), 'plain', 'utf-8')
        message['From'] = Header("%s"%(Name), 'utf-8')
        message['To'] = Header("jiayuguang@qq.com")
        message['Subject'] = Header("%s"%(Header_show),'utf-8')
        return message


    def Send(self,message):
        '''

        :param message:发送信息
        :return:
        '''
        self.smtpObj=smtplib.SMTP('smtp.163.com')
        self.smtpObj.set_debuglevel(1)
        self.smtpObj.login(self.sender,self.password)
        self.smtpObj.sendmail(self.sender,self.receivers,message.as_string())
        return self.smtpObj

    def Quit(self):
        self.smtpObj.quit()



class SSHsign_in(object):
    '''ssh-执行脚本'''

    def __init__(self,host,port,username,password):
        '''
        :param host: ip地址
        :param port: 端口号
        :param username: 用户名
        :param password: 密码
        '''
        self.host=host
        self.port=port
        self.username=username
        self.password =password
        self.ssh_rd=None

    def SSH_ready(self):
        self.ssh_rd = paramiko.SSHClient()
        try:
            self.ssh_rd.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_rd.connect(
                self.host,
                port=self.port,
                username=self.username,
                password=self.password,
            )

        except  Exception:
            logging.warning("SSH_ready error",Exception)
        return self.ssh_rd

    def SSH_implement(self,cmd):
        return self.ssh_rd.exec_command(cmd)

    def SSH_close(self):
        self.ssh_rd.close()












