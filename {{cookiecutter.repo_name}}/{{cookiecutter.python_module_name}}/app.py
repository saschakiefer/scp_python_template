import os

from .{{cookiecutter.python_module_name}} import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")
