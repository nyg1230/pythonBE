import logging
import logging.config
import os
from operator import itemgetter
from app.common.util import property_util

global LOGGER_CONFIG
LOGGER_CONFIG = property_util.get_prop("logger")

def load_logger():
    path, config = itemgetter("path", "config")(LOGGER_CONFIG)
    handlers = config.get("handlers")
    for v in dict(handlers).values():
        if "filename" in v.keys():
            v["filename"] = f"{path}/{v.get('filename')}"

    if (not os.path.exists(path)): os.makedirs(path)
    logging.config.dictConfig(config)

class Logger():
    _levels = ["debug", "info", "warning", "error", "critical"]
    def __init__(self, name = None):
        self._logger = logging.getLogger(name)
        # level = LOGGER_CONFIG.get("level")
        # self._level = level if level in self._levels else "info"
        self._level = "info"
        _level = getattr(logging, self._level.upper())
        self._logger.setLevel(_level)
        # self._logger_path = LOGGER_CONFIG["path"] or "./log"
        self._logger_path = "./log"

    def set_console_logger(self, format, level = "info"):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self.get_level(level))
        stream_handler.setFormatter(logging.Formatter(format))
        self._logger.addHandler(stream_handler)

    def set_file_logger(self, filename, format, level = "info"):
        if (not os.path.exists(self._logger_path)): os.makedirs(self._logger_path)
        full_path = f"{self._logger_path}/{filename}.log"
        file_handler = logging.FileHandler(full_path)
        file_handler.setLevel(self.get_level(level))
        file_handler.setFormatter(logging.Formatter(format))
        self._logger.addHandler(file_handler)
        
    def log(self, message):
        self._logger.log(self._logger.level, message)
        
    def get_level(self, level = "info"):
        level = level if level in self._levels else "info"
        return getattr(logging, level.upper())

    def all_clear_handler(self):
        for handler in self._logger.handlers:
            self._logger.removeHandler(handler)