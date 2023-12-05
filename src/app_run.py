from flask import Flask
from operator import itemgetter
import logging
from flask_cors import CORS
from app.common.util import blueprint_util, property_util, logger_util
from app.common.decorator import decorator
from app.common.exception import exception_handler

# logger setting
logger_util.load_logger()
logger = logging.getLogger("app_logger")

app = Flask(__name__)
CORS(app, resources={r"/*": { "origins": "*" }})
st_msg = "server start"
logger.log(logging.INFO, st_msg)

# blueprint regist
bp_regist_info = blueprint_util.blueprint_regist(app)
success, fail = itemgetter("success", "fail")(bp_regist_info)
fail_count = 0
fail_detail = []
for k, v in dict(fail).items():
    fail_count += list(v).__len__()
    fail_detail.append(f"\t\t{k}: {v}")
fail_detail = "\n".join(fail_detail)
be_msg = f'''blueprint regist complete
\tsuccess: {success}
\tfail - count({fail_count})
{fail_detail}'''
logger.log(logging.INFO, be_msg)

# decorator regist
decorator.regist_request_decorator(app)
deco_msg = "flask decorator regist complete"
logger.log(logging.INFO, deco_msg)

# exception handler regist
exception_handler.regist_handler(app)
exp_handler_msg = "exception handler regist complete"
logger.log(logging.INFO, exp_handler_msg)

host, port, debug = itemgetter("host", "port", "debug")(property_util.get_server())
run_msg = f'''server run complete
    {host}:{port}, Debug: {debug}'''
logger.log(logging.INFO, run_msg)

if __name__ == '__main__':
    app.run(host = host, port = port, debug = debug)