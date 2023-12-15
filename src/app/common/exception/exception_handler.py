from flask import Flask, jsonify, Response
from app.common.exception.custom_exception import CustomException

# 로깅 작업하기
def regist_handler(app: Flask):
    @app.errorhandler(Exception)
    def common_exception_handler(e: Exception):
        print(e)
        test = { "name": "test exception", "code": "t001" }
        return Response(jsonify(test), 400)
    
    @app.errorhandler(CustomException)
    def custom_exception_handler(e: CustomException):
        return Response(e.to_json(), e.get_status_code())
