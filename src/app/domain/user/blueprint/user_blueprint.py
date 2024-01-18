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

@user.route("/login", methods = ["POST"])
@decorator.issue_token_by_user
def login():
    json = request.get_json()
    user = UserVo(**json)
    user = user_service.find_by_account(user)

    if (user is None):
        raise CustomException(ExcpetionCode.NOT_EXIST_USER)
    else:
        if (not user.check_pw(json.get("pwd"))):
            raise CustomException(ExcpetionCode.LOGIN_FAIL)

    return user

@user.route("/doubleCheck", methods = ["POST"])
def doubleCheck():
    json = request.get_json()
    user = UserVo(**json)
    user = user_service.find_by_account(user)

    result = { "duplicate": user is not None }

    return result

@user.route("/signup", methods = ["POST"])
def signup():
    json = request.get_json()
    user = UserVo().create(**json)
    result = user_service.signup(user)

    return { "state": "?" }

@user.route("/get", methods = method_enum.get("CRUD"))
@decorator.jwt_authorization
def get_user():
    token = jwt_util.create_token({ "test": 1 })
    return token