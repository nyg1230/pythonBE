from flask import Blueprint, request, Response, jsonify
from app.common.decorator import decorator
from app.domain.account.service.account_service import AccountService
from app.domain.account.vo.account_vo import AccountVo

import json

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
@decorator.data_to_json
def get_account():
    json = request.get_json()
    result = account_service.select_account(json)

    return result

@account.route("/update", methods = ["POST"])
@decorator.jwt_authorization
def update_account():
    json = request.get_json()
    account = AccountVo(**json)
    
    account_service.update(account)
    
    return Response(status=200)

@account.route("/period/data", methods = ["POST"])
@decorator.jwt_authorization
@decorator.data_to_json
def get_period_expense():
    json = request.get_json()
    result = account_service.select_period_data(json)
    
    return result

@account.route("/period/category/data", methods = ["POST"])
@decorator.jwt_authorization
def get_period_category_expense():
    req_json = request.get_json()
    result = account_service.select_period_category_data(req_json)
    
    return json.dumps(result, default=str, ensure_ascii=False)