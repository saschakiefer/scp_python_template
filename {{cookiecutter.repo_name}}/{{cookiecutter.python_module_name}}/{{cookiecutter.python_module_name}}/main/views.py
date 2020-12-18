from cfenv import AppEnv
from flask import request, abort
from sap import xssec

from . import main

env = AppEnv()
uaa_service = env.get_service(
    name="{{ cookiecutter.uaa_service_instance_name }}"
).credentials


@main.route("/", methods=["GET"])
def main_route():
    # check if authorization information is provided
    if "authorization" not in request.headers:
        abort(403)

    # check if user is authorized
    access_token = request.headers.get("authorization")[7:]
    security_context = xssec.create_security_context(access_token, uaa_service)
    is_authorized = security_context.check_scope("openid")
    is_authorized = security_context.check_scope("$XSAPPNAME.user")

    if not is_authorized:
        abort(403)

    return security_context._properties
