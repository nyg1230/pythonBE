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
@decorator.jwt_authorization
def add_tag():
    json = request.get_json()
    tag = tag_service.create_tag(json)

    return tag.to_json()

@tag.route("/remove", methods = ["POST"])
@decorator.jwt_authorization
def remove_tag():
    json = request.get_json()
    tag_service.delete_tag(json)

    return "remove tag"