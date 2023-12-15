from flask import Flask, jsonify, request, Response
import json
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
        jwt = headers.get(jwt_util.JWTEnum.HEADER.value)
        jwt_util.validate_token(jwt)

        return f(*args, **kwargs)
    
    return deco

def issue_token_by_user(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        user = f(*args, **kwargs)
        token = jwt_util.create_token(user.get_token_info())
        return Response(user.to_json(), headers={ f"{jwt_util.JWTEnum.HEADER.value}": token }, mimetype="application/json")
    return wrapper

def reissue_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        output = f(*args, **kwargs)
        return output
    return wrapper
