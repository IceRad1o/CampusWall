#-*- coding:utf-8 -*-
import json
from BaseHandlerh import BaseHandler
from Database.tables import Activity, ActivityComment
from Activity.Activityfunc import Commentfunc

class Activitycomment(BaseHandler):
    retjson ={'code':'200','contents':'none'}
    def post(self):
        type = self.get_argument('type',default='null')
        if type == '10090': #评论
            m_acid = self.get_argument('acid',default='null')
            m_phone = self.get_argument('phone',default='null')
            m_comment = self.get_argument('comment',default='null')
            try:
                comac = self.db.query(Activity).filter(Activity.Acid == m_acid).one
                newcom = ActivityComment(

                ActivityAcid = m_acid,
                Comertel = m_phone,
                Comcontent = m_comment,
                )
                self.db.merge(newcom)
                self.db.commit()
                self.retjson['code']='10091'
                self.retjson['contents']='评论成功'

            except Exception,e:
                print e
                self.retjson['code']='10092'
                self.retjson['contents']='不存在此活动！'
        if type =='10093':#查看评论
            m_acid = self.get_argument('acid', default='null')
            retdata=[]
            try:
                comac = self.db.query(Activity).filter(Activity.Acid == m_acid).one

                allcomment= self.db.query(ActivityComment).filter(ActivityComment.ActivityAcid==m_acid).all()
                for item in allcomment:
                    Commentfunc(item,retdata)
                self.retjson['code']='10094'
                self.retjson['contents']=retdata
            except Exception, e:
                print e
                self.retjson['code'] = '10095'
                self.retjson['contents'] = '不存在此活动！'

        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))