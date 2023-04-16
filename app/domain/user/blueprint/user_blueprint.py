from flask import Blueprint

user = Blueprint("user_blueprint", __name__, url_prefix="/user")

@user.route("/get")
def get_user():
    return "test"