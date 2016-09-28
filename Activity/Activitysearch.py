#-*- coding:utf-8 -*-
import json

from BaseHandlerh import BaseHandler
from Database.tables import Activity
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
        self.write(json.dumps(self.retjson, ensure_ascii=False, indent=2))

