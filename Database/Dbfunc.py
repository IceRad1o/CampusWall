# -*- coding: utf-8 -*-

class Dbfuncs(object):

    @staticmethod
    def commit_error(self, retjson, e):
        '''
        Args:
            retjson: 修改的json
            e: 异常
        '''
        retjson['contents'] = '数据库更新错误'
        retjson['code'] = '10274'

def call_back(value):
    print 'call back value:', value

def caller(func, arg):
    print 'caller'
    func(arg)

caller(call_back, 'hello,world')