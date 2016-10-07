#-*- coding:utf-8 -*-
'''
author:wjl 2016-10-6

'''
from BaseHandlerh import BaseHandler
from qiniu import Auth
class AuthkeyHandler:
    def __init__(self):
        self.access_key = 'qRfWWS5sGsp6vGMTFQ29QGeRzAF-4BdEQPVFTQK2'
        self.secret_key = 'udSOvCkppV4-4eXc8nCYDBuVnaE4e0sqVFErKuAY'
        self.Auth_key = Auth(self.access_key, self.secret_key)
        self.auth_tokens = []

    def generateToken(self, names):
        bucket_name = 'campuswall'  # 要上传的空间
        tokens = []
        for title in names:
            print 'title:', title
            token = self.Auth_key.upload_token(bucket_name, title, 345600)
            self.auth_tokens.append(token)
        return self.auth_tokens

    def get_auth_key(self):
        return self.Auth_key

    def get_token(self):
        return self.auth_tokens

    def download_url(self, name):
        auth = self.get_auth_key()
        bucket_domain = 'oektidosb.bkt.clouddn.com'
        base_url = 'http://%s/%s' % (bucket_domain, name)
        private_url = auth.private_download_url(base_url, expires=3600)
        return private_url


