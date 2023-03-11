from flask import Flask
from app.common.config import regist_blueprint
from common.config import Config
from common.exception import error_handler

app = Flask(__name__)

regist_blueprint.auto_register(app)
error_handler.ErrorHandler(app)
server_config = Config.ServerConfig()

if __name__ == '__main__':
    app.run(
        host    = server_config.get_host(),
        port    = server_config.get_port(),
        debug   = server_config.get_debug()
    )