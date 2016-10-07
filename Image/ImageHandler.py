#-*- coding:utf-8 -*-
'''
author:wjl 2016-10-6

'''
import time

from Database.models import get_db
from Database.tables import UserImage, Image,Activityimage


class ImageHandler(object):
    def insert(self,list):
        '''
        向数据库插入图片链接
        :param list: 图片名的列表
        :table: 应该插入的表名
        :return:
        '''
        new_imids=[]
        for img_name in list:  # 第一步，向Image里表里插入
            image = Image(
                IMvalid=True,
                IMT=time.strftime('%Y-%m-%d %H:%M:%S'),
                IMname = img_name
            )
            db=get_db()
            db.merge(image)
            db.commit()
            new_img = get_db().query(Image).filter(Image.IMname == img_name).one()
            imid = new_img.IMid
            new_imids.append(imid)
        return new_imids

    def insert_user_image(self, list, utel):
        '''

        Args:
            list:图片名字的数组
            uid: 用户的手机

        Returns:

        '''
        imids = self.insert(list)
        for i in range(len(imids)):
            image = UserImage(
                Uimagetel=utel,
                UIimid=imids[i],
                Uurl=list[i]
            )
            db = get_db()
            db.merge(image)
            db.commit()

    def change_user_headimage(self, newimage, utel):
        db = get_db()
        images = db.query(UserImage).filter(UserImage.Uimagetel == utel).all()
        for image in images:
            image_id = image.UIimid
            im = db.query(Image).filter(Image.IMid == image_id).one()
            if im.IMvalid == 1:
                im.IMvalid = 0
        db.commit()
        self.insert_user_image(newimage, utel)

    def insert_activity_image(self, list, ac_id):
        '''

        Args:
            list: 图片的名字的数组
            ac_id: 活动的ID

        Returns:

        '''
        imids = self.insert(list)
        for i in range(len(imids)):
            image = Activityimage(
                Aimageid=ac_id,
                ACIimid=imids[i],
                Acimgurl=list[i]
            )
            db = get_db()
            db.merge(image)
            db.commit()