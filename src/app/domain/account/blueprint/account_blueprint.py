from flask import Blueprint, request, Response, jsonify
from app.common.decorator import decorator
from app.domain.account.service.account_service import AccountService

account = Blueprint("account_blueprint", __name__, url_prefix="/account")
account_service = AccountService()

@account.route("/list/add", methods = ["POST"])
@decorator.jwt_authorization
def add_list():
    json = request.get_json()
    print(json)
    account_list = json["list"]
    account_service.add_account_list(account_list)

    return Response(status=200)
