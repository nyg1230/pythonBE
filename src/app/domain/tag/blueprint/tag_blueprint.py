from flask import Blueprint, request
from app.domain.tag.service.tag_service import TagService
from app.domain.tag.vo.tag_vo import TagVo
from app.common.util import jwt_util
from app.common.decorator import decorator
from app.common.exception.custom_exception import CustomException
from app.common.exception.exception_code import ExcpetionCode

tag = Blueprint("tag_blueprint", __name__, url_prefix="/tag")
tag_service = TagService()

@tag.route("/add", methods = ["POST"])
@decorator.issue_token_by_user
def add_tag():
    json = request.get_json()
    print(json)
    
    return "add tag"

@tag.route("/remove", methods = ["POST"])
@decorator.issue_token_by_user
def remove_tag():
    json = request.get_json()
    print(json)

    return "remove tag"