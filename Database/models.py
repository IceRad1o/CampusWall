# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

from sqlalchemy.orm import scoped_session, sessionmaker

reload(sys)
sys.setdefaultencoding('utf8')  # python的str默认是ascii编码，和unicode编码冲突,需处理

DB_CONNECT_STRING = 'mysql+mysqldb://root@127.0.0.1/campuswall?charset=utf8'
#DB_CONNECT_STRING = 'mysql+mysqldb://root:ydrs.sql.7234@localhost:3306/Shacus?charset=utf8'
#DB_CONNECT_STRING = 'mysql+mysqldb://root:seuwjl@localhost:3306/campuswall?charset=utf8'
#  pool_recycle=10
engine = create_engine(DB_CONNECT_STRING, echo=True, pool_size=100, max_overflow=300)  # 返回数据库引擎，即连接数据库
connection = engine.connect()

Base = declarative_base()  # declarative_base() 创建了一个 BaseModel 类，这个类的子类可以自动与一个表关联。
                           # Construct a base class for declarative class definitions.

if(engine!=None):
    print "数据库连接成功，return"
    Base.metadata.create_all(engine)
    print connection

else:
    print "未找到数据库"

db2 = None
def get_db():
    '''

    Returns:返回数据库操作session

    '''
    global db2
    #if not db:
    db2 = scoped_session(sessionmaker(bind=engine,
                                         autocommit=False, autoflush=True,
                                         expire_on_commit=False))
    return db2


