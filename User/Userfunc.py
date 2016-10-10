# -*- coding:utf-8 -*-

from Database.models import get_db
from Database.tables import User, UserImage, Image
from Image.Upload import AuthkeyHandler

def Userfunc(item,retdata):
    auth = AuthkeyHandler()
    userurl = get_db().query(UserImage).filter(UserImage.Uimagetel==item.Utel).all()
    url = []
    for user_headimage in userurl:
        exist = get_db().query(Image).filter(Image.IMid == user_headimage.UIimid, Image.IMvalid == 1).all()
        if exist:
            url = user_headimage
            break;

    try:
        if item.Ubirthday:
            Ubirthday = User.Ubirthday.strftime('%Y-%m-%d %H:%M:%S'),
        else:
            Ubirthday = ''
    except Exception, e:
        print e
        Ubirthday = ''
    if url:
        m_Userfunc=dict(
            Uid=item.Uid,
            Upassword=item.Upassword,
            Utel=item.Utel,
            Ualais=item.Ualais, # 昵称
            Uname = item.Uname , # 真实姓名
            Uschool = item.Uschool ,  # 学校
            Umailbox = item.Umailbox ,  # unique=True) # unique表示唯一性
            Ubirthday = Ubirthday ,
            Uscore =item.Uscore ,
            UregistT = item.UregistT.strftime('%Y-%m-%dT%H:%M:%S') ,
            Usex =item.Usex ,
            Usign =item.Usign,
            Userurl = auth.download_url(url.Uimgurl)
        )
        retdata.append(m_Userfunc)
    else:
        m_Userfunc = dict(
            Uid=item.Uid,
            Upassword=item.Upassword,
            Utel=item.Utel,
            Ualais=item.Ualais,  # 昵称
            Uname=item.Uname,  # 真实姓名
            Uschool=item.Uschool,  # 学校
            Umailbox=item.Umailbox,  # unique=True) # unique表示唯一性
            Ubirthday=Ubirthday,
            Uscore=item.Uscore,
            UregistT=item.UregistT.strftime('%Y-%m-%dT%H:%M:%S'),
            Usex=item.Usex,
            Usign=item.Usign,
            Userurl=''
        )
        retdata.append(m_Userfunc)


