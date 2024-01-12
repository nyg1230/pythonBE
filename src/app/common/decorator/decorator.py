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
        jwt = jwt_util.get_current_token()
        jwt_util.validate_token(jwt)

        return f(*args, **kwargs)
    
    return deco

def issue_token_by_user(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        user = f(*args, **kwargs)
        token = jwt_util.create_token(user.get_token_info())
        headers = {
            "Access-Control-Expose-Headers": jwt_util.JWTEnum.HEADER.value,
            f"{jwt_util.JWTEnum.HEADER.value}": token
        }
        
        try:
            jwt_util.validate_token(token)
        except:
            print(1)

        return Response(user.to_json(), headers=headers, mimetype="application/json")
    return wrapper

def reissue_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        output = f(*args, **kwargs)
        return output
    return wrapper


def sql_logging(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        output = f(*args, **kwargs)
        return output
    return wrapper