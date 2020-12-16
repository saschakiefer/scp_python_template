import os

from flask import Flask
from flask_cors import CORS

from .config import config

here = os.path.split(__file__)[0]


def create_app(config_name):
    app = Flask(__name__)

    print(f"Loading '{config_name}' configuration")

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    CORS(app, resources={r"*": {"origins": "*"}})

    # Register blueprints
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
