from flask import Blueprint, request
from app.domain import method_enum
from app.domain.user.service.user_service import UserService
from app.common.util import jwt_util
from app.common.decorator import decorator

user = Blueprint("user_blueprint", __name__, url_prefix="/user")

@user.route("/login", methods = ["POST"])
def login():
    json = request.get_json()
    return { "test": { "qwer": 123, "asdf": [1,2,3,4], "zxcv": { "a": 1 } } }

@user.route("/signup", methods = ["POST"])
def signup():
    print("qwer")
    return { "state": "?" }

@user.route("/get", methods = method_enum.get("CRUD"))
@decorator.jwt_authorization
def get_user():
    token = jwt_util.create_token({ "test": 1 })
    return token