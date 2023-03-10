from flask import Flask
import importlib

BLUEPRINT_LIST = [
    { "path": "domain.user.blueprint.user_blueprint", "name": "user_page" }
]

def auto_register(app: Flask):
    for blueprint in BLUEPRINT_LIST:
        module = importlib.import_module(blueprint["path"], package="app")
        bp = getattr(module, blueprint["name"])
        app.register_blueprint(bp)