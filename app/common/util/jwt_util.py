from datetime import datetime
import jwt
from enum import Enum
import date_util
from app.common.exception.exception_code import ExcpetionCode
from app.common.exception.custom_exception import CustomException

class JWTEnum(Enum):
    KEY = "nope"
    ALG = "HS256"
    EXP_PERIOD = 5 * 60 * 1000
    EXP_UNIT = "ms"

def create_token(param):
    now_datetime = datetime.utcnow()
    payload = {
        "issuedAt": "",
        "exp": date_util.add_datetime_unit_2_ts(now_datetime, JWTEnum.EXP_PERIOD.value, JWTEnum.EXP_UNIT.value)
    }
    token = jwt.encode(payload, JWTEnum.KEY.value, JWTEnum.ALG.value)
    return token

def recreate_token(token):
    if (validate_token(token)): return
    re_token = create_token()
    return re_token

def validate_token(token):
    try:
        jwt.decode(token, JWTEnum.KEY.value, JWTEnum.ALG.value)
    except jwt.ExpiredSignatureError:
        raise CustomException(ExcpetionCode.JWT_EXPIRED_PERIOD)
    except jwt.InvalidTokenError:
        raise CustomException(ExcpetionCode.JWT_INVALID)
    return True