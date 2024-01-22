from flask import Flask, jsonify, request, Response
import json
from functools import wraps
from app.common.util import jwt_util, common_util
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

        output = f(*args, **kwargs)
        
        new_jwt = jwt_util.recreate_token(token = jwt)
        headers = {
            "Access-Control-Expose-Headers": jwt_util.JWTEnum.HEADER.value,
            f"{jwt_util.JWTEnum.HEADER.value}": new_jwt
        }
        
        return Response(output, headers=headers)
    
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

def data_to_json(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        output = fn(*args, **kwargs)
        
        result = None
        try:
            data = output.get("data")
            if (common_util.is_list(data)):
                result = []
                for vo in data:
                    result.append(vo.to_dict())
                # result = json.dumps(result, default=str, ensure_ascii=False)
            else:
                result = data.to_dict()

            output.__setitem__("data", result)
        except:
            result = output

        return json.dumps(output, default=str, ensure_ascii=False)
    return wrapper

def sql_logging(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        output = f(*args, **kwargs)
        return output
    return wrapper