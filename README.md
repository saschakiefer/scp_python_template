# scp_python_template

[Cookiecutter](https://cookiecutter.readthedocs.io) template for creating a simple
PaaS application ready to deploy to [SAP Cloud Platform](https://www.sap.com/germany/products/cloud-platform.html)

## Features

- Flask application container with `main` blueprint
- AppRouter module to protect the application from unauthorized users
- Example Role implemented
- Local test possible

## Prerequisite

You need to have cookiecutter installed (e.g. with `pip install --user cookiecutter` or with `brew install cookiecutter`).

## Create Project

If you want to get the host prefix and the app domain prefilled, you need to checkout the
template locally and run the `cookiecutter_runner` python script with 
```bash
git checkout git@github.com:saschakiefer/scp_python_template.git
cd /path/to/project/home
python path/to/git/scp_python_template/cookiecutter_runner.py
```

Since this option reads the infrastructure data from `~/.cf/config.json` you need to have the 
`cf` CLI installed and have logged in to your subaccount/space.

Alternatively you can call `cookiecutter https://github.com/saschakiefer/scp_python_template.git`
from the `/path/to/project/home`. In this case, however, the infrastructure values are
not prefilled. This command clones the template locally to `~/.cookiecutters`. So subsequently,
you can call `python ~/.cookiecutters/scp_python_template/cookiecutter_runner.py`.
