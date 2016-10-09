#-*- coding:utf-8 -*-
from Database.models import get_db
from Database.tables import User, Favorite, UserImage, Image, Activityimage
from Image.Upload import AuthkeyHandler


def Activityfunc(item,userphone,retdata):
    #活动返回模型

    auth = AuthkeyHandler()
    test01 = get_db().query(User).filter(User.Uid == item.Acsponsorid).one()
    test = get_db().query(UserImage).filter(UserImage.Uimagetel == test01.Utel).all()
    url=[]
    for user_headimage in test:
        exist = get_db().query(Image).filter(Image.IMid == user_headimage.UIimid, Image.IMvalid == 1).all()
        if exist:
                url = user_headimage
                break;
    #返回发起活动的用户的头像

    aclurl = get_db().query(Activityimage).filter(Activityimage.Aimageid == item.Acid).limit(1).all()

    #:返回活动图片




    nickname = get_db().query(User).filter(item.Acsponsorid==User.Uid).all()
    acisliked = 0
    try:
        acinfo = get_db().query(Favorite).filter(Favorite.Facid == item.Acid,Favorite.Futel == userphone).one()
        if acinfo.Fvalid == 0:
            acisliked = 0
        elif acinfo.Fvalid == 1:
            acisliked = 1
    except Exception,e:
        print e
        acisliked = 0
    if aclurl:
        m_Activity=dict(
            Acid=item.Acid,
            Acsponsorname = nickname[0].Ualais,
            Acsponsorid=item.Acsponsorid,
            Acsponsorimg = auth.download_url(url.Uimgurl),
            Acimgurl = auth.download_url(aclurl[0]. Acimgurl),
            AcsponsT=item.AcsponsT.strftime('%Y-%m-%dT%H:%M:%S'),
            AccommentN=item.AccommentN,
            AclikeN=item.AclikeN,
            Accontent=item.Accontent,
            Actitle=item.Actitle,
            Acisliked = acisliked,
            niming = item.niming
        )
        retdata.append(m_Activity)
    else:
        m_Activity = dict(
            Acid=item.Acid,
            Acsponsorname=nickname[0].Ualais,
            Acsponsorid=item.Acsponsorid,
            Acsponsorimg=auth.download_url(url.Uimgurl),
            Acimgurl='',
            AcsponsT=item.AcsponsT.strftime('%Y-%m-%dT%H:%M:%S'),
            AccommentN=item.AccommentN,
            AclikeN=item.AclikeN,
            Accontent=item.Accontent,
            Actitle=item.Actitle,
            Acisliked=acisliked,
            niming=item.niming
        )
        retdata.append(m_Activity)




def Commentfunc(item,retdata):
    auth = AuthkeyHandler()

    test = get_db().query(UserImage).filter(UserImage.Uimagetel == item.Comertel).all()
    url = []
    for user_headimage in test:
        exist = get_db().query(Image).filter(Image.IMid == user_headimage.UIimid, Image.IMvalid == 1).all()
        if exist:
            url = user_headimage
            break;
            # 返回发起活动的用户的头像
    id = get_db().query(User).filter(User.Utel==item.Comertel).all()
    Comment = dict(

    Commentid= item.Commentid,
    Comertel = item.Comertel,
    Comerimgurl = auth.download_url(url.Uimgurl),
    ComerUalais = id[0].Ualais,
    Comcontent = item.Comcontent,


    )
    retdata.append(Comment)

