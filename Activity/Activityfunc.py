#-*- coding:utf-8 -*-
from Database.models import get_db
from Database.tables import User, Favorite


def Activityfunc(item,userphone,retdata):
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
    m_Activity=dict(
        Acid=item.Acid,
        Acsponsorname = nickname[0].Ualais,
        #Acresponsorimg=item.Acsponsorimg,
        Acsponsorid=item.Acsponsorid,
        AcsponsT=item.AcsponsT.strftime('%Y-%m-%dT%H:%M:%S'),
        AccommentN=item.AccommentN,
        AclikeN=item.AclikeN,
        Accontent=item.Accontent,
        Actitle=item.Actitle,
        Acisliked = acisliked,
    )
    retdata.append(m_Activity)
def Commentfunc(item,retdata):
    Comment = dict(

    Commentid= item.Commentid,
    Comertel = item.Comertel,
    Comcontent = item.Comcontent,

    )
    retdata.append(Comment)

