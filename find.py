from typing import Union
from db_models import UserInfoDB, CnAreaDB, RecordDB
from db import SessionLocal
from sqlalchemy import and_
from sqlalchemy import desc
from typing import List

#针对UserInfoDB进行查询
#根据openid获取userinfo
def find_userinfo_by_openid(openid: str) -> Union[UserInfoDB, None]:
    with SessionLocal() as sess:
        return sess.query(UserInfoDB).filter_by(openid=openid).order_by(desc(UserInfoDB.id)).first()

#针对CnAreaDB进行查询
#根据level获取merger_name
def find_merger_name_by_level(level: int) -> Union[CnAreaDB, None]:
    with SessionLocal() as sess:
        return sess.query(CnAreaDB).filter_by(level=level).all()
    
#根据name获取areacode
def find_area_code_by_name(name: str) -> Union[CnAreaDB, None]:
    with SessionLocal() as sess:
        return sess.query(CnAreaDB).filter_by(name=name).first()
    
#根据areacode获取areas
def find_areas_by_area_code(narea_code: int) -> Union[CnAreaDB, None]:
    with SessionLocal() as sess:
        return sess.query(CnAreaDB).filter(
            and_(CnAreaDB.area_code > narea_code,
                 CnAreaDB.area_code < narea_code + 100000)
            ).all()

#针对RecordDB进行查询
#根据openid获取record
def find_record_by_openid(openid: str) -> Union[RecordDB, None]:
    with SessionLocal() as sess:
        return sess.query(RecordDB).filter_by(openid=openid).all()

#根据id获取record
def find_record_by_id(openid: str) -> Union[RecordDB, None]:
    with SessionLocal() as sess:
        return sess.query(RecordDB).filter_by(id=id).first()
    
#根据address获取record
def find_record_by_address(address: str) -> Union[RecordDB, None]:
    with SessionLocal() as sess:
        return sess.query(RecordDB).filter_by(address=address).all()

#根据address获取符合条件的record的行数
def find_record_counts_by_address(address: str) -> int:
    with SessionLocal() as sess:
        return sess.query(RecordDB).filter_by(address=address).count()
