#-*- coding:utf-8 -*-
import json

from sqlalchemy import desc

from Activity import Activityfunc
from BaseHandlerh import BaseHandler
from Database.tables import Activity, User


class ActivityaskHandler(BaseHandler):

    def post(self):
        retjson = {'code': '200', 'contents': 'null'}
        retdata = []
        type = self.get_argument('type', default='unsolved')
        if type == '12001':  # 请求刷新所有动态
            u_id = self.get_argument('uid', default='null')
            try:
                data = self.db.query(Activity).filter(Activity.ACvalid == 1).order_by(
                    desc(Activity.AcsponsT)).all()
                length = len(data)
                print length
                if length < 10:
                    for i in range(length):
                        datauser = self.db.query(User).filter(data[i].Acsponsorid == User.Uid).one()
                        Activityfunc.Activityfunc(datauser,retdata)
                        self.retjson['code'] = '10303'
                        self.retjson['contents'] = retdata
            except Exception,e:
                print e

        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))  # 返回中文