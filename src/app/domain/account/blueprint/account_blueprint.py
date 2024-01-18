from flask import Blueprint, request, Response, jsonify
from app.common.decorator import decorator
from app.domain.account.service.account_service import AccountService

account = Blueprint("account_blueprint", __name__, url_prefix="/account")
account_service = AccountService()

@account.route("/add", methods = ["POST"])
@decorator.jwt_authorization
def add_account():
    json = request.get_json()
    account_list = json["list"]
    account_service.insert_account(account_list)

    return Response(status=200)

@account.route("/get", methods = ["POST"])
@decorator.jwt_authorization
@decorator.vo_to_json
def get_account():
    json = request.get_json()
    result = account_service.select_account(json)

    return result