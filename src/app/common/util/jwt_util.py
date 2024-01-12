import jwt
from flask import request
from datetime import datetime, timedelta
from enum import Enum
from app.common.util import date_util
from app.common.exception.exception_code import ExcpetionCode
from app.common.exception.custom_exception import CustomException
from app.domain.user.vo.user_vo import UserVo

class JWTEnum(Enum):
    HEADER = "X-AUTH-TOKEN"
    RT = "X-AUTH-RT"
    AT = "X-AUTH-AT"
    KEY = "nope"
    ALG = "HS256"
    EXP_PERIOD = 30 * 60

def get_payload(token):
    validate_token(token)
    return jwt.decode(token, JWTEnum.KEY.value, JWTEnum.ALG.value)

def create_token(p: dict):
    now = datetime.utcnow()
    payload = {
        **p,
        "iss": "",
        "sub": "",
        "iat": now,
        "exp": now + timedelta(seconds = JWTEnum.EXP_PERIOD.value)
    }

    token = jwt.encode(payload, JWTEnum.KEY.value, algorithm = JWTEnum.ALG.value)

    return token

def recreate_token(token):
    payload = get_payload(token)
    now_timestamp = date_util.get_now_timestamp()
    dict(payload).setdefault("iat", now_timestamp)
    dict(payload).setdefault("exp", now_timestamp + JWTEnum.EXP_PERIOD.value)
    return create_token(payload)

def validate_token(token):
    try:
        jwt.decode(token, JWTEnum.KEY.value, JWTEnum.ALG.value)
    except jwt.ExpiredSignatureError:
        raise CustomException(ExcpetionCode.JWT_EXPIRED_PERIOD)
    except jwt.InvalidTokenError:
        raise CustomException(ExcpetionCode.JWT_INVALID)
    return True

def get_current_token():
    headers = request.headers
    jwt = headers.get(JWTEnum.HEADER.value)
    return jwt

def get_current_user():
    jwt = get_current_token()
    payload = get_payload(jwt)
    
    return payload
    