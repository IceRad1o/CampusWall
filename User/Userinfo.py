# -*- coding:utf-8 -*-
import json
from BaseHandlerh import BaseHandler
from Database.tables import User
from User import Userfunc


class Userinfo(BaseHandler):
    retjson = {'code': '200', 'contents': 'none'}
    def post(self):
        type = self.get_argument('type',default='unsolved')

        if type =='10020': #请求用户具体信息
            retdata=[]
            m_phone = self.get_argument('phone',default='null')
            try:
                infomation=self.db.query(User).filter(m_phone == User.Utel).one()
                Userfunc.Userfunc(infomation,retdata)
                self.retjson['code']='10021'
                self.retjson['contents']=retdata
            except Exception,e:
                print e
                self.retjson['code']='10022'
                self.retjson['contents']='查找出现错误'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))
