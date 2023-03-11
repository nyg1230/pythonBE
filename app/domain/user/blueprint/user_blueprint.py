from flask import Blueprint, request
from domain.user.exception.user_error_info import UserErrorInfo
from common.exception.custom_exception import CustomException

user_page = Blueprint("user_page", __name__, url_prefix="/user")

@user_page.route("/get/<int:oid>", methods=["GET"])
def get_user(oid):
    if (oid == 123):
        print(UserErrorInfo.USER_NOT_EXIST)
    return { "oid": oid }

@user_page.route("/test")
def test():
    raise CustomException(UserErrorInfo.USER_NOT_EXIST)
    return {}