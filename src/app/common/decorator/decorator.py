from flask import Flask, request
from functools import wraps
from enum import Enum
import logging

logger = logging.getLogger("info_logger")

# 로그에 출력할 내용 작업하기
def regist_request_decorator(app: Flask):
    @app.before_request
    def before_req():
        msg = f"{request.path}"
        logger.log(logging.INFO, msg)
        print(request.path)

def jwt_authorization(f):
    @wraps(f)
    def deco(*args, **kwargs):
        print("jwt_authorization >>>>>>>>>>>>>>>>>>>>>>")
        print(request)
        return f(*args, **kwargs)
    
    return deco
