from flask import Blueprint, request
from app.domain.tag.service.tag_service import TagService
from app.domain.tag.vo.tag_vo import Vo
from app.common.util import jwt_util
from app.common.decorator import decorator
from app.common.exception.custom_exception import CustomException
from app.common.exception.exception_code import ExcpetionCode

tag = Blueprint("tag_blueprint", __name__, url_prefix="/tag")
tag_service = TagService()

@tag.route("/sample", methods = [])
@decorator.issue_token_by_user
def sample():
    return "sample"