#-*- coding:utf-8 -*-
import json

from BaseHandlerh import BaseHandler
from Database.tables import User, Activity


class ActivityPublish(BaseHandler):
   retjson = {'code': '200', 'contents': 'null'}
   def post(self):
       type = self.get_argument('type',default='unsolved')
       if type == '10040':
           m_title = self.get_argument('title',default='null')
           m_category = self.get_argument('category',default='null')
           m_author = self.get_argument('author',default='null')
           m_content = self.get_argument('content',default='null')
           try:
                userid=self.db.query(User).filter(User.Utel==m_author).one()
                m_id = userid.Uid
                my_activity = Activity(
                    Acsponsorimg='',
                    Acsponsorid=m_id,
                    #AcsponsT='0000-00-00 00:00:00',
                    AccommentN=0,
                    AclikeN=0,
                    Accontent=m_content,
                    Actitle=m_title,
                    Acvalid=1,
                    Accategory=m_category

                )
                self.db.merge(my_activity)
                self.db.commit()
                self.retjson['code'] = '10041'
                self.retjson['contents'] = '发布成功'
           except Exception,e:
               print e
               self.retjson['code'] = '10042'
               self.retjson['contents'] = '发布失败'

       self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))  # 返回中文








