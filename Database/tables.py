# -*- coding: utf-8 -*-
from sqlalchemy import Boolean
from sqlalchemy import CHAR
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import VARCHAR
from sqlalchemy.sql.functions import func
from models import Base
import sys
reload(sys)

# 每个类对应一个表
class User(Base): # 用户表   #添加聊天专用chattoken
    __tablename__ = 'User'

    Uid = Column(Integer, nullable=False, primary_key=True)  # 主键
    Upassword = Column(VARCHAR(16), nullable=False)
    Utel = Column(CHAR(11),nullable=False,unique=True,)
    Ualais = Column(VARCHAR(24),nullable=False,unique=True) # 昵称
    Uname = Column(VARCHAR(24),nullable=True) # 真实姓名
    Uschool = Column(VARCHAR(128))#学校
    Umailbox = Column(VARCHAR(32))#unique=True) # unique表示唯一性
    Ubirthday = Column(DateTime)
    Uscore = Column(Integer, default=0)
    UregistT = Column(DateTime(timezone=True), default=func.now())
    Usex = Column(Boolean,nullable=False)
    Usign = Column(VARCHAR(256))
    #Uauthkey = Column(VARCHAR(32))

class Activity(Base):
    __tablename__ = 'Activity'
    Acid = Column(Integer, primary_key=True)
    Acsponsorimg = Column(VARCHAR(128), nullable=False)
    Acsponsorid = Column(Integer, ForeignKey('User.Uid', onupdate='CASCADE'), primary_key=True)  # 用户id
    AcsponsT = Column(DateTime(timezone=True), default=func.now())  # 时间
    AccommentN = Column(Integer, nullable=False, default=0)
    AclikeN = Column(Integer, nullable=False, default=0)
    Accontent = Column(VARCHAR(128), nullable=False)
    Actitle = Column(VARCHAR(12), nullable=False)
    Acvalid = Column(Boolean, nullable=False, default=1)

class Favorite(Base):
    __tablename__ = 'Favorite'

    Fid = Column(Integer, primary_key=True)
    Fuid = Column(Integer, ForeignKey('User.Uid', onupdate='CASCADE'), nullable=False)
    #Ftype = Column(Integer, nullable=False, default=0)
    Ftypeid = Column(Integer, nullable=False, default=0)
    FT = Column(DateTime(timezone=True), default=func.now())
    Fvalid = Column(Boolean, nullable=False, default=1)


