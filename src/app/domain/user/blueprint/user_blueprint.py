from flask import Blueprint, request
from app.domain import method_enum
from app.domain.user.service.user_service import UserService
from app.domain.user.vo.user_vo import UserVo
from app.common.util import jwt_util
from app.common.decorator import decorator
from app.common.exception.custom_exception import CustomException
from app.common.exception.exception_code import ExcpetionCode

user = Blueprint("user_blueprint", __name__, url_prefix="/user")
user_service = UserService()

@user.route("/login", methods = ["GET", "POST"])
def login():
    user = UserVo()
    user = user_service.find_by_account(user)
    token = None

    if (user is None):
        raise CustomException(ExcpetionCode.NOT_EXIST_USER)
    else:
        if (user.check_pw("")):
            token = jwt_util.create_token(user.get_token_info())
        else:
            raise CustomException(ExcpetionCode.LOGIN_FAIL)

    return { "token": token }

@user.route("/signup", methods = ["POST"])
def signup():
    print("qwer")
    return { "state": "?" }

@user.route("/get", methods = method_enum.get("CRUD"))
@decorator.jwt_authorization
def get_user():
    token = jwt_util.create_token({ "test": 1 })
    return token