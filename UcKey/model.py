#!/usr/bin/python
#coding=utf-8


from __future__ import unicode_literals
from Tools.SomeTool import *
import pymysql
import datetime
from _models.models import LoginMsg
db_show = pymysql.connect(host="123.57.226.182",user="root",passwd="Jksd3344",db="Shake",charset="utf8")
db = db_show.cursor()

# Create your models here.



class Pmsg(object):

    def count_sql(self,sql):
        try:
            db.execute(sql)
            num = int(list(db.fetchall()[0])[0])
            db_show.commit()
            return num
        except Exception:
            print("the Pmsg.take_sql is error%s"% Exception)


    def SaveLoginMsg(self,data):
        Find_sql="select count(*) from LoginMsg WHERE uid = %s"%data.get("uid")
        Uid=self.count_sql(Find_sql)

        if Uid==0:
            some = LoginMsg.objects.create(
                uid=data.get("uid"),
                name=data.get("name"),
                account=data.get("account"),
                phone=data.get("phone"),
                number=data.get("number"),
                sex=data.get("sex"),
                email=data.get("email"),
                department_id=data.get("department_id"),
                role_name=data.get("role_name"),
            )
            self.Send_some_mail(data.get("email"),data.get("name"))
        else:
            some=LoginMsg.objects.filter(uid=data.get("uid","")).update(
                uid=data.get("uid"),
                name=data.get("name"),
                account=data.get("account"),
                phone=data.get("phone"),
                number=data.get("number"),
                sex=data.get("sex"),
                email=data.get("email"),
                department_id=data.get("department_id"),
                role_name=data.get("role_name"),
                killtime=datetime.datetime.now(),
            )
        return some

    def Send_some_mail(self,email,name):
        Sm=Send_mail("jksd517@163.com","1234liuxin",["jiayuguang@qq.com"])
        msg=Sm.Re_msg("%s首次登陆系统,您的所有操作已经被记录在案,感谢您的使用...."%name,"数据中心","系统给你打了声招呼")
        Sm.Send(msg)
        Sm.Quit()