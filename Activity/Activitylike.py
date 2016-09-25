#-*- coding:utf-8 -*-
import json

from BaseHandlerh import BaseHandler
from Database.tables import Favorite, Activity


class Activitylike(BaseHandler):
    retjson = {'code': '200', 'contents': '活动操作'}
    def post(self):
        type = self.get_argument('type',default='unsolved')
        if type == '10060':#点赞
            acid = self.get_argument('acid',default='null')
            m_phone = self.get_argument('phone',default='null')
            try:
                ifActivity = self.db.query(Activity).filter(Activity.Acid == acid).one()
                try:
                    Aclike = self.db.query(Favorite).filter(Favorite.Facid == acid,Favorite.Futel == m_phone).one()
                    if Aclike.Fvalid == 1:
                        self.retjson['code']='10062'
                        self.retjson['contents']='已经点过赞!不能重复点赞'
                    elif Aclike.Fvalid == 0:
                        Aclike.Fvalid = 1
                        ifActivity.AclikeN += 1
                        self.db.commit()
                        self.retjson['code'] = '10061'
                        self.retjson['contents']='点赞成功'
                except Exception,e:
                    print e
                    newaclike = Favorite (
                        Futel = m_phone,
                        Facid=acid,
                        Fvalid = 1
                    )
                    self.db.merge(newaclike)
                    ifActivity.AclikeN += 1
                    self.db.commit()
                    self.retjson['code']='10061'
                    self.retjson['contents']='点赞成功!'
            except Exception,e:
                print e
                self.retjson['code']='10062'
                self.retjson['contents']='该活动不存在'

        if type == '10070':  # 取消点赞
            acid = self.get_argument('acid', default='null')
            m_phone = self.get_argument('phone', default='null')
            try:
                ifActivity = self.db.query(Activity).filter(Activity.Acid == acid).one()
                try:
                    Aclike = self.db.query(Favorite).filter(Favorite.Facid == acid, Favorite.Futel == m_phone).one()
                    if Aclike.Fvalid == 0:

                        self.retjson['code'] = '10072'
                        self.retjson['contents'] = '没有对该活动点过赞'
                    elif Aclike.Fvalid == 1:
                        Aclike.Fvalid = 0
                        ifActivity.AclikeN -= 1
                        self.db.commit()
                        self.retjson['code'] = '10071'
                        self.retjson['contents'] = '取消点赞成功'
                except Exception, e:
                    self.retjson['code'] = '10072'
                    self.retjson['contents'] = '没有对该活动点过赞2'
            except Exception, e:
                print e
                self.retjson['code'] = '10062'
                self.retjson['contents'] = '该活动不存在'
        if type == '10080':
            acid = self.get_argument('acid', default='null')
            m_phone = self.get_argument('phone', default='null')
            retdata = {'isliked':'null'}
            try:
                ifActivity = self.db.query(Activity).filter(Activity.Acid == acid).one()
                if ifActivity:
                    try:
                        Aclike = self.db.query(Favorite).filter(Favorite.Facid == acid, Favorite.Futel == m_phone).one()
                        retdata['isliked']= Aclike.Fvalid
                        if Aclike.Fvalid==1:
                            self.retjson['code']='10081'
                        elif Aclike.Fvalid==0:
                            self.retjson['code'] = '10082'
                        self.retjson['contents']=retdata
                    except Exception,e:
                        print e
                        self.retjson['code']='10083'
                        self.retjson['contents']='查询失败！'


            except Exception,e:
                print e
                self.retjson['code']='10083'
                self.retjson['contents']='没有此活动！'


        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))  # 返回中文

