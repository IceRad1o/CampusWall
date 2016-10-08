# -*- coding:utf-8 -*-
import json
from BaseHandlerh import BaseHandler
from Database.tables import User
from Image.ImageHandler import ImageHandler
from Image.Upload import AuthkeyHandler


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

        elif type == '10110':#要求上传头像，返回token
            #u_id = self.get_argument('uid')
            image = self.get_argument('image')
            image_token_handler = AuthkeyHandler()
            #jsont = "{'fuck':'exome??'}"
            m_image_json = json.loads(image)
            self.retjson['contents'] = image_token_handler.generateToken(m_image_json)
            self.retjson['code'] = '10111'


        elif type == '10120':
            u_tel = self.get_argument('utel')
            image = self.get_argument('image')
            m_image_json = json.loads(image)
            auth = AuthkeyHandler()
            im = ImageHandler()
            im.change_user_headimage(m_image_json, u_tel)
            self.retjson['contents'] = auth.download_url(m_image_json[0])
            self.retjson['code'] = '66666'

        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))
