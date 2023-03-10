from flask import Blueprint, request

user_page = Blueprint("user_page", __name__, url_prefix="/user")

@user_page.route("/get/<int:oid>", methods=["GET"])
def get_user(oid):
    print("test")
    print("oid")
    return { "oid": oid }