#-*- coding:utf-8 -*-
from Database.models import get_db
from Database.tables import User


def Activityfunc(item,retdata):
    nickname = get_db().query(User).filter(item.Acsponsorid==User.Uid).all()
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
    )
    retdata.append(m_Activity)

