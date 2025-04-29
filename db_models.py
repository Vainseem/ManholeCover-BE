from sqlalchemy import Column, String, DateTime, Integer, Numeric, TEXT
from db import Base

class UserInfoDB(Base):
    __tablename__ = "userinfo"

    id           = Column(Integer,       primary_key=True, autoincrement=True)
    openid       = Column(String(64),    nullable=True)
    nickname     = Column(String(64),    nullable=True)
    timestamp1   = Column(DateTime,      nullable=True)
    headimgurl   = Column(TEXT(65535),   nullable=True)
    telephone    = Column(String(16),    nullable=True)

class CnAreaDB(Base):
    __tablename__ = 'cnarea_2023'

    id          = Column(Integer,        primary_key=True)
    level       = Column(Integer,        nullable=False, comment='层级')
    parent_code = Column(Integer,        nullable=False, default=0,  comment='父级行政代码')
    area_code   = Column(Integer,        nullable=False, default=0,  comment='行政代码')
    zip_code    = Column(Integer,        nullable=False, default=0,  comment='邮政编码')
    city_code   = Column(String(6),      nullable=False, default='', comment='区号')
    name        = Column(String(50),     nullable=False, default='', comment='名称')
    short_name  = Column(String(50),     nullable=False, default='', comment='简称')
    merger_name = Column(String(50),     nullable=False, default='', comment='组合名')
    pinyin      = Column(String(30),     nullable=False, default='', comment='拼音')
    lng         = Column(Numeric(10, 6), nullable=False, default=0.000000, comment='经度')
    lat         = Column(Numeric(10, 6), nullable=False, default=0.000000, comment='纬度')


class RecordDB(Base):
    __tablename__ = 'records'

    id         = Column(Integer, primary_key=True, autoincrement=True)
    openid     = Column(String(64),    nullable=True)
    timestamp2 = Column(DateTime,      nullable=True)
    image      = Column(TEXT(65535),   nullable=True)
    status     = Column(Integer,       nullable=True)
    address    = Column(String(64),    nullable=True)
    remakes    = Column(String(64),    nullable=True)