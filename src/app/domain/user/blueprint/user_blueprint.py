from flask import Blueprint, request
from app.domain import method_enum
from app.domain.user.service.user_service import UserService
from app.common.util import jwt_util

user = Blueprint("user_blueprint", __name__, url_prefix="/user")

@user.route("/get", methods = method_enum.get("CRUD"))
def get_user():
    token = jwt_util.create_token({ "test": 1 })
    return token