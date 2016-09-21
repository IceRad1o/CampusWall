# -*- coding:utf-8 -*-
from Database.tables import User


def Userfunc(item,retdata):
    try:
        if item.Ubirthday:
            Ubirthday = User.Ubirthday.strftime('%Y-%m-%d %H:%M:%S'),
        else:
            Ubirthday = ''
    except Exception, e:
        print e
        Ubirthday = ''
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
    )
    retdata.append(m_Userfunc)

