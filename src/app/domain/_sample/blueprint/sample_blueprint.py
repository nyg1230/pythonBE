from flask import Blueprint, request
from app.domain._sample.service.sample_service import SampleService
from app.domain._sample.vo.vo import Vo
from app.common.util import jwt_util
from app.common.decorator import decorator
from app.common.exception.custom_exception import CustomException
from app.common.exception.exception_code import ExcpetionCode

sample = Blueprint("sample_blueprint", __name__, url_prefix="/sample")
sample_service = SampleService()

@sample.route("/sample", methods = [])
@decorator.issue_token_by_user
def sample():
    return "sample"