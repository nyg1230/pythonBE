from flask import Flask
from app.common.util import blueprint_util, property_util, logger_util
from app.common.decorator import decorator
from app.common.exception import exception_handler
from operator import itemgetter

# 하위 함수 확인 후 호출 함수 반환받아서 로깅 작업하기
app = Flask(__name__)
logger_util.load_logger()
blueprint_util.blueprint_regist(app)
decorator.regist_request_decorator(app)
exception_handler.regist_handler(app)
host, port, debug = itemgetter("host", "port", "debug")(property_util.get_server())

if __name__ == '__main__':
    app.run(host = host, port = port, debug = debug)