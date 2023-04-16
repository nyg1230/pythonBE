from flask import Flask
from app.common.util import blueprint_util, property_util
from app.common.exception import exception_handler
from operator import itemgetter

app = Flask(__name__)
blueprint_util.blueprint_regist(app)
exception_handler.regist_handler(app)
host, port, debug = itemgetter("host", "port", "debug")(property_util.get_server())

if __name__ == '__main__':
    app.run(host = host, port = port, debug = debug)