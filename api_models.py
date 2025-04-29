from __future__ import annotations
from pydantic import BaseModel as PydanticBaseModel
from typing import Optional
import datetime

#配置pydantic允许接受任意类型的数据作为输入
class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class Status(BaseModel):
    status: int = 0


class UserInfoAPI(BaseModel):
    id:         int                         = None  #数据库主键指定id
    openid:     str                         = None  #用户平台唯一id
    nickname:   Optional[str]               = None  #昵称
    timestamp1: Optional[datetime.datetime] = None  #上次登陆时间
    headimgurl: Optional[str]               = None  #头像，采用base64字符串进行存贮
    telephone:  Optional[str]               = None  #联系方式


class CnAreaAPI(BaseModel):
    id:          int    # ID
    level:       int    # 层级
    parent_code: int    # 父级行政代码
    area_code:   int    # 行政代码
    zip_code:    int    # 邮政编码
    city_code:   str    # 区号
    name:        str    # 名称
    short_name:  str    # 简称
    merger_name: str    # 组合名
    pinyin:      str    # 拼音
    lng:         float  # 经度
    lat:         float  # 纬度


class RecordAPI(BaseModel):
    id:         int                         = None  #数据库主键指定id
    openid:     str                         = None  #提交记录的用户
    timestamp2: Optional[datetime.datetime] = None  #记录提交时间
    image:      Optional[str]               = None  #上传图片，采用base64进行存贮
    status:     Optional[str]               = None  #状态码
    address:    Optional[str]               = None  #上传记录地址，拼接规则示例：四川,成都,金牛,凤凰山
    remakes:    Optional[str]               = None  #备注

