from flask import Blueprint, request
from app.domain import method_enum
from app.domain.user.service.user_service import UserService

user = Blueprint("user_blueprint", __name__, url_prefix="/user")

@user.route("/get", methods = method_enum.get("CRUD"))
def get_user():
    try:
        user_info = UserService().find_by_oid(1234)
    except Exception as e:
        print(e)
    return f"{user_info}"