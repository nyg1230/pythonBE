from flask import Flask, jsonify
from app.common.exception.custom_exception import CustomException

def regist_handler(app: Flask):
    @app.errorhandler(Exception)
    def common_exception_handler(e: Exception):
        test = { "name": "test exception", "code": "t001" }
        return jsonify(test, 400)
    
    @app.errorhandler(CustomException)
    def custom_exception_handler(e: CustomException):
        error_info = e.get_error_info()
        return error_info
