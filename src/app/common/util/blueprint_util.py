from enum import Enum
from flask import Flask
import importlib

class blueprint_enum(Enum):
    user = "app.domain.user.blueprint.user_blueprint"
    board = "app.domain.board.blueprint.board_blueprint"

def blueprint_regist(app: Flask):
    result = {
        "success": [],
        "fail": {}
    }
    for blueprint in blueprint_enum:
        key = blueprint.name
        path = blueprint.value
        try:
            module = importlib.import_module(path, package="app")
            blueprint_module = getattr(module, key)
            app.register_blueprint(blueprint_module)
            result["success"].append(key)
        except Exception as e:
            fail = result["fail"]
            name = type(e).__name__
            fail.setdefault(name, [])
            fail[name].append(key)
    return result