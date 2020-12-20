from cookiecutter.main import cookiecutter

import json
import os.path
from pathlib import Path

curdir = os.path.dirname(os.path.abspath(__file__))

extra_context = {}

try:
    # read cf config file
    with open(os.path.join(Path.home(), ".cf/config.json"), "r") as cf_config:
        data = cf_config.read()

    # parse file
    obj = json.loads(data)

    extra_context["scp_app_host_prefix"] = (
        obj["OrganizationFields"]["Name"] + "-" + obj["SpaceFields"]["Name"] + "-"
    )

    extra_context["scp_app_domain"] = "cfapps" + obj["Target"][14:]

except FileNotFoundError:
    pass


cookiecutter(curdir, extra_context=extra_context, overwrite_if_exists=False)
