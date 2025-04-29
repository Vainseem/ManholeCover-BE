#以下为fastapi配置

from fastapi import HTTPException

from typing import Union

from fastapi.responses import RedirectResponse

from pydantic import BaseModel

from fastapi import Header, Cookie

from fastapi import FastAPI, Request, Body

from fastapi.exceptions import RequestValidationError

from fastapi.responses import JSONResponse

from fastapi import Depends

#以上为fastapi

#以下为Email配置

import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

from email import encoders

import uvicorn
#以上为Email

#以下为Email依赖函数

def send_mail_util(content, file_path=None):  #Email

    try:

        if (not type(content) is str):
            return [0, "FBC001", "邮件内容参数类型错误,不为字符串", [None]]
        #要发送的邮件默认为字符串，并且不许回车

        sender = '3037917066@qq.com'
        receiver = 'ysq15083558865@qq.com'
        subject = 'ManholesCover'
        password = 'fqmcqrjtmfudddci'
        email_host = "smtp.qq.com"
        receivers = [receiver]
        send_user = "<" + sender + ">"
        #一些基本的信息，在这里调整邮件发送邮箱,接受邮箱,邮件标题,服务器与发送邮箱的密码

        message = MIMEMultipart()
        message['Subject'] = subject
        message['From'] = send_user
        message['To'] = ";".join(receivers)
        message.attach(MIMEText(content, 'plain', 'utf-8'))
        #调整邮件内容格式

        if file_path:
            with open(file_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {file_path}")
                message.attach(part)
        #预留的邮件附件发送功能，但是没跟前端说（）

        server = smtplib.SMTP_SSL(email_host, 465)
        server.login(sender, password)
        server.sendmail(sender, receivers, message.as_string())
        server.quit()
        #偷偷登一下邮箱，发个邮件然后退出

        print('邮件发送成功')
        return [1, '000000', '邮件发送成功', [receivers[0]]]

    except Exception as e:
        print("邮件发送失败异常," + str(e))
        return [0, 'FBE999', "邮件发送失败异常," + str(e), [None]]
    #成功就扣1，000000，失败就报错打印错误信息

#以上为依赖函数

#以下为fastapi主体

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/EmailSending/")
async def Email(content: str=Body(1,title='content',embed=True)):
    result = send_mail_util(content)
    return result

@app.get("/ping/")
async def Ping(ans: str):
    ans = "pong"
    return ans
#以上为fastapi主体