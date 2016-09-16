#-*- coding:utf-8 -*-
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    @property  # python装饰器把一个方法变成属性调用

    def db(self):
        return self.application.db

    def on_finish(self):
        self.db.close()
