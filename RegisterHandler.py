# -*- coding:utf-8 -*-
import json
import random
import time
from sqlalchemy import desc
import datetime

from BaseHandlerh import BaseHandler
from Database.tables import User


class RegisterHandler(BaseHandler):
    print "进入regist"
    retjson = {'code': '400', 'contents': 'None'}
    def post(self):
        type = self.get_argument('type', default='unsolved')
        if type == '10001':  # 验证手机号
            m_phone=self.get_argument('phone')
            try:
                user = self.db.query(User).filter(User.Utel == m_phone).one()
                if user:
                    self.retjson['contents'] = u"该手机号已经被注册，请更换手机号或直接登录"
                    self.retjson['code'] = '10005'
            except Exception,e:
                print e
                self.retjson['code']='10006'
                self.retjson['contents']='可以注册了'
        elif type == '10002':  # 注册详细信息
            m_password = self.get_argument('password')
            m_nick_name = self.get_argument('nickname')  # 昵称
            m_phone = self.get_argument('phone')
            m_school=self.get_argument('school')
            #m_auth_key = generate_auth_key()
            retdata = []
            retdata_body = {}
            new_user = User(
                Upassword=m_password,
                Ualais=m_nick_name,
                Uname='',
               # Ulocation='',  # 新用户注册默认level为1
                Umailbox='',
                Ubirthday='0000-00-00 00:00:00',
                Uschool=m_school,
                Utel=m_phone,
                Uscore=0,
                Usex=1,
                Usign='',

            )
            self.db.merge(new_user)
            self.db.commit()
            self.retjson['code']='10003'
            self.retjson['contents']='注册成功'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))



