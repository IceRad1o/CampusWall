#-*- coding:utf-8 -*-
import json
from tokenize import String

from sqlalchemy import distinct

from BaseHandlerh import BaseHandler
from Database.tables import Activity, User, Favorite, ActivityComment
from Activity.Activityfunc import Activityfunc

class Activitysearch(BaseHandler):
    retjson={'code':'200','contents':'null'}
    def post(self):
        type = self.get_argument('type',default='10100')
        if type == '10100':
            retdata=[]
            m_phone = self.get_argument('phone',default='null')
            searchurl = self.get_argument('searchurl',default='null')
            url = '%'+searchurl+'%'
            contents = self.db.query(Activity).filter(Activity.Accontent.like(url)).all()
            for search in contents:
                Activityfunc(search,m_phone,retdata)

            self.retjson['code']='10101'
            self.retjson['contents']=retdata
        elif type == '12001':#返回所有此用户发布的活动
            retdata= []
            m_phone = self.get_argument('phone',default='null')
            try:
                uid = self.db.query(User).filter(m_phone==User.Utel).one()
                allac = self.db.query(Activity).filter(Activity.Acsponsorid ==uid.Uid).all()
                for item in allac:
                    Activityfunc(item,m_phone,retdata)
                self.retjson['code'] = '12002'
                self.retjson['contents'] = retdata

            except Exception,e:
                print e
                self.retjson['code'] = '12003'
                self.retjson['contents'] = "没有此用户"

        elif type == '12004':#查看用户所有点赞的活动
            retdata = []
            m_phone = self.get_argument('phone', default='null')
            alllikeac = self.db.query(Favorite).filter(Favorite.Futel==m_phone,Favorite.Fvalid==1).all()
            x=len(alllikeac)
            if  x:
                for item in alllikeac:
                    try:
                        acliked = self.db.query(Activity).filter(item.Facid==Activity.Acid,Activity.Acvalid==1).one()
                        Activityfunc(acliked, m_phone, retdata)
                    except Exception,e:
                        print e
                self.retjson['code'] = '12005'
                self.retjson['contents'] = retdata
            else:
                self.retjson['code'] = '12006'
                self.retjson['contents'] = '用户尚未点过赞'
        elif type == '12007':#查看用户所有评论的活动
            retdata = []
            m_phone = self.get_argument('phone', default='null')

            allcomac = self.db.query(distinct(ActivityComment)).filter(ActivityComment.Comertel == m_phone, ActivityComment.Comvalid == 1).all()
            # x = len(allcomac)
            # list =[]
            # for i in range(x):
            #      list.append(allcomac[i])
            # print allcomac,'哈哈哈哈哈哈哈'
            # print list
            for allcomac_item in allcomac:
                print allcomac_item,'哈哈哈哈哈'
                acliked = self.db.query(Activity).filter(Activity.Acid == allcomac_item.ActivityAcid ,Activity.Acvalid == True,).one()
                Activityfunc(acliked, m_phone, retdata)
                self.retjson['code'] = '12008'
                self.retjson['contents'] = retdata

        elif type== '12100':
            allcomac = self.db.query(ActivityComment).filter(ActivityComment.Commentid==1).all()
            for allcomac_item in allcomac:
                acliked = self.db.query(Activity).filter(Activity.Acid == allcomac_item.ActivityAcid,Activity.Acvalid == True).one()
            #print 'hhhhhh',acliked






        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))

