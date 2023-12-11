from flask import Flask, request
from functools import wraps
from app.common.util import jwt_util
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
        headers = request.headers
        jwt = headers.get(jwt_util.JWTEnum.HEADER)
        jwt_util.validate_token(jwt)

        return f(*args, **kwargs)
    
    return deco
