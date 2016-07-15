#!/usr/bin/python
#coding=utf-8

import time
import hashlib
import requests
import json
# Create your views here.



class AccessApi(object):

    '''
        current_method:发送命令(可选)
        callback_url:发送回调地址(可选)
        url_path:访问地址(定值)

        ('loginUrl',"http://%s/userscheck/" % host,'common/rpc')
    '''
    def __init__(self,current_method,callback_url,url_path):
        self.settings = {
            'api_url' : 'http://api.ucenter.playcrab.com/',
            'api_key' : '3158308647',
            'api_secret_key' : '454fceaa64e202256b295a7184272af4'
        }
        self.data={
            "callback":callback_url
        }
        self.params = {
            'id': '1',
            'method': current_method,
            'params': self.data,
            'jsonrpc': '2.0'
        }

        self.ApiUrl="%s%s" % (self.settings['api_url'],url_path)
        self.header_authorization_prefix = "PLAYCRAB"



    def post(self):
        '''访问'''

        header=self.ReHeader(self.params)
        r=requests.post(self.ApiUrl,data=json.dumps(self.params),headers=header)
        return json.loads(r.text)



    def ReHeader(self,params):
        '''获取访问头'''

        date = time.strftime('%Y-%m-%dT%X+08:00', time.localtime())
        token_str = '%s%s%s' % (self.convertDictToStr({'params': params}), self.settings['api_secret_key'], date)
        token = hashlib.md5(token_str.encode(encoding="utf-8"))
        authorization = "%s %s:%s" % (self.header_authorization_prefix, self.settings['api_key'], token.hexdigest())
        header = {'Content-Type': 'application/json', 'Date': date, 'Authorization': authorization}
        return header


    def convertDictToStr(self,params):
        '''字典转化成字符串'''

        glue=""
        param_data = params.get('params', '')
        str_data = ''

        for k , v in param_data.items():
            if type(v) == tuple or type(v) == list or type(v) == dict:
                v = sorted(v)
                tmp_str = glue.join(v)
                str_data += k + tmp_str + glue
            else:
                str_data += k + v + glue
        return str_data