from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware

from db import init_database
from . import login, location, record

WECHAT_APP_ID = 'wxff510f8e3bfa2d82'
WECHAT_APP_SECRET = '8a16e5c72a5b89943b7863581ee7e558'
WECHAT_SESSION = 'https://api.weixin.qq.com/sns/jscode2session'

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 头部
)


app.include_router(login.loginRouter)
app.include_router(location.locationRouter)
app.include_router(record.recordRouter)


@app.on_event("startup")
async def startup():
    """startup event"""

    # 初始化数据库
    init_database()

@app.get('/ping')
def pong():
    """healthcheck"""
    return Response(content='pong')
