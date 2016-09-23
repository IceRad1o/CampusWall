#-*- coding:utf-8 -*-
import json

from sqlalchemy import desc

from Activity import Activityfunc
from BaseHandlerh import BaseHandler
from Database.tables import Activity, User


class ActivityaskHandler(BaseHandler):
    retjson = {'code': '200', 'contents': 'null'}
    def post(self):

        retdata = []
        type = self.get_argument('type', default='unsolved')
        if type == '10050':  # 请求刷新所有动态
            try:
                data = self.db.query(Activity).filter(Activity.Acvalid == 1).order_by(
                    desc(Activity.AcsponsT)).all()
                length = len(data)
                print length
                if length < 10:
                    for i in range(length):
                        Activityfunc.Activityfunc(data[i],retdata)
                        self.retjson['code'] = '10303'
                        self.retjson['contents'] = retdata
                else:
                    for item in range(0,10):
                        Activityfunc.Activityfunc(data[item], retdata)
                        self.retjson['code'] = '10303'
                        self.retjson['contents'] = retdata
            except Exception,e:
                print e

        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))  # 返回中文