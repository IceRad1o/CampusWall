# -*- coding:utf-8 -*-
import json
from BaseHandlerh import BaseHandler
from Database.tables import User


class Usersetting(BaseHandler):
    retjson={'code':'200','contents':'none'}
    def post(self):
        type = self.get_argument('type',default='unsloved')
        if type == '10030':
            m_phone = self.get_argument('phone',default='null')
            m_nickname =self.get_argument('nickname',default='null')
            m_password =self.get_argument('password',default='null')
            m_school=self.get_argument('school',default='null')
            m_signature=self.get_argument('signature',default='null')
            try:
                setting = self.db.query(User).filter(User.Utel==m_phone).one()
                setting.Upassword = m_password
                setting.Ualais = m_nickname
                setting.Uschool = m_school
                setting.Usign= m_signature
                self.db.commit()
                self.retjson['code']='10031'
                self.retjson['contents']=r"修改用户信息成功！"
            except Exception,e:
                print e
                self.retjson['code']='10032'
                self.retjson['contents']='用户修改失败'
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))