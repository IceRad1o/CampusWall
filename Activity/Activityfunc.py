#-*- coding:utf-8 -*-
def Activityfunc(item,retdata):

    m_Activity=dict(
        Acid=item.Acid,
        #Acresponsorimg=item.Acsponsorimg,
        Acsponsorid=item.Acsponsorid,
        AcsponsT=item.AcsponsT.strftime('%Y-%m-%dT%H:%M:%S'),
        AccommentN=item.AccommentN,
        AclikeN=item.AclikeN,
        Accontent=item.Accontent,
        Actitle=item.Actitle,
    )
    retdata.append(m_Activity)

