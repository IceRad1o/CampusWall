#-*- coding:utf-8 -*-
import json

from sqlalchemy import desc

from Activity import Activityfunc
from BaseHandlerh import BaseHandler
from Database.tables import Activity, User


class ActivityaskHandler(BaseHandler):

    def post(self):
        retjson = {'code': '200', 'contents': 'null'}
        type = self.get_argument('type', default='unsolved')
        m_sortby=self.get_argument('sortby',default='null')
        m_phone = self.get_argument('phone',default='null')
        if type == '10050':  # 请求刷新所有动态
            retdata = []
            try:
                if m_sortby == 'time':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1).order_by(
                        desc(Activity.AcsponsT)).all()
                elif m_sortby == 'like':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1).order_by(
                        desc(Activity.AclikeN)).all()
                elif m_sortby == 'comment':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1).order_by(
                        desc(Activity.AccommentN)).all()
                length = len(data)
                print length
                if length < 10:
                    for i in range(length):
                        Activityfunc.Activityfunc(data[i],m_phone,retdata)
                        retjson['code'] = '10054'
                        retjson['contents'] = retdata
                else:
                    for item in range(0,10):
                        Activityfunc.Activityfunc(data[item],m_phone,retdata)
                        retjson['code'] = '10054'
                        retjson['contents'] = retdata
            except Exception,e:
                print e
        if type == '10051':  # 请求刷新所有1 动态
            retdata = []
            try:
                if m_sortby == 'time':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==1).order_by(
                        desc(Activity.AcsponsT)).all()
                elif m_sortby == 'like':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==1).order_by(
                        desc(Activity.AclikeN)).all()
                elif m_sortby == 'comment':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==1).order_by(
                        desc(Activity.AccommentN)).all()
                length = len(data)
                print length
                if length < 10:
                    for i in range(length):
                        Activityfunc.Activityfunc(data[i],m_phone,retdata)
                        retjson['code'] = '10055'
                        retjson['contents'] = retdata
                else:
                    for item in range(0,10):
                        Activityfunc.Activityfunc(data[item],m_phone, retdata)
                        retjson['code'] = '10055'
                        retjson['contents'] = retdata
            except Exception,e:
                print e
        if type == '10052':  # 请求刷新所有 2 动态
            retdata = []
            try:
                if m_sortby == 'time':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==2).order_by(
                        desc(Activity.AcsponsT)).all()
                elif m_sortby == 'like':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==2).order_by(
                        desc(Activity.AclikeN)).all()
                elif m_sortby == 'comment':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==2).order_by(
                        desc(Activity.AccommentN)).all()
                length = len(data)
                print length
                if length < 10:
                    for i in range(length):
                        Activityfunc.Activityfunc(data[i],m_phone,retdata)
                        retjson['code'] = '10056'
                        retjson['contents'] = retdata
                else:
                    for item in range(0,10):
                        Activityfunc.Activityfunc(data[item],m_phone, retdata)
                        retjson['code'] = '10056'
                        retjson['contents'] = retdata
            except Exception,e:
                print e
        if type == '10053':  # 请求刷新所有 3 动态
            retdata = []
            try:
                if m_sortby == 'time':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==3).order_by(
                        desc(Activity.AcsponsT)).all()
                elif m_sortby == 'like':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==3).order_by(
                        desc(Activity.AclikeN)).all()
                elif m_sortby == 'comment':
                    data = self.db.query(Activity).filter(Activity.Acvalid == 1,Activity.Accategory==3).order_by(
                        desc(Activity.AccommentN)).all()
                length = len(data)
                print length
                if length < 10:
                    for i in range(length):
                        Activityfunc.Activityfunc(data[i],m_phone,retdata)
                        retjson['code'] = '10057'
                        retjson['contents'] = retdata
                else:
                    for item in range(0,10):
                        Activityfunc.Activityfunc(data[item],m_phone, retdata)
                        retjson['code'] = '10057'
                        retjson['contents'] = retdata
            except Exception,e:
                print e

        self.write(json.dumps(retjson, ensure_ascii=False, indent=2))  # 返回中文