from enum import Enum
from flask import Flask
import importlib

class blueprint_enum(Enum):
    user = "app.domain.user.blueprint.user_blueprint"
    board = "app.domain.board.blueprint.board_blueprint"

def blueprint_regist(app: Flask):
    success = []
    fail = []
    for blueprint in blueprint_enum:
        is_success = False
        key = blueprint.name
        path = blueprint.value
        try:
            module = importlib.import_module(path, package="app")
            blueprint_module = getattr(module, key)
            app.register_blueprint(blueprint_module)
            success.append(key)
            is_success = True
        except ModuleNotFoundError as e:
            print("fail call blueprint module...")
        except AttributeError as e:
            print("wrong module attribute...")
        except Exception as e:
            print(e)
        finally:
            print(f"{key}:\t{path}")
            if (is_success == False): fail.append(key)
    print("registed list")
    print(f"success -\t{success}")
    print(f"fail -\t\t{fail}")