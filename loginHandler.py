# -*- coding:utf-8 -*-
import json

from BaseHandlerh import BaseHandler
from Database.tables import User


class loginHandler(BaseHandler):
    retjson={'code':'200','contents':'none'}
    retdata=[]
    print '进入登录'
    def post(self):
        type=self.get_argument('type','unsolved')
        if type=='10010':
            m_phone=self.get_argument("phone",default='none')
            m_password=self.get_argument('password',default='none')
            try:
                user=self.db.query(User).filter(m_phone==User.Utel).one()
                try:
                    pawd=self.db.query(User).filter(user.Upassword==m_password).one()
                    if pawd:
                        self.retjson['code']='10011'
                        self.retjson['contents']='登录成功'
                except Exception,e:
                    self.retjson['code']='10012'
                    self.retjson['contents']='输入密码错误'
            except Exception,e:
                print e
                self.retjson['code']='10012'
                self.retjson['contents'] = '没有此帐号'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))  # 返回中文