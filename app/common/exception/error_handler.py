from flask import Flask, jsonify
from common.exception.custom_exception import CustomException

def ErrorHandler(app: Flask):
    @app.errorhandler(Exception)
    def common_handler(e):
        info = {
            "error": "Error",
            "message": "message"
        }
        return jsonify(info, 500)
    
    @app.errorhandler(CustomException)
    def custom_handler(e):
        return e.get_error_info()