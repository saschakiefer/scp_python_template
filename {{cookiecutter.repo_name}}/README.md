# {{cookiecutter.project_name}}

Simple SAP Cloud Platform PaaS App. Written in Python with Flask and protected by the AppRouter.

## Deployment
### Pre Deployment
You have to be logged in to your cloud platform service account.

Before you can deploy the application, you have to create a `xsuaa` service instance with
```bash
cf create-service xsuaa application {{ cookiecutter.uaa_service_instance_name }} -c xs-security.json
```

### Deployment
You can deploy the app with `cf push`.

### Post Deployment

After the deployment you have to create a Role Collection which contains the `User`-role (alternatively you can add the role to an existing role collection).
This role collection needs to be assigned to the user to logon.

## Local Testing
### Prerequisite
- `node` version: `^12.0.0`
- you have deployed the application once to CF
- you are logged on to your SCP space

### AppRouter
#### Configure Connection to XSUAA
Create a service key for accessing XSUAA and get the key values:
```bash
cf create-service-key {{ cookiecutter.uaa_service_instance_name }} {{ cookiecutter.uaa_service_instance_name }}-key
cf service-key {{ cookiecutter.uaa_service_instance_name }} {{ cookiecutter.uaa_service_instance_name }}-key
```

Copy the output ant place it into the `{{cookiecutter.approuter_module_name}}/default-service.json` file 
(replace the empty object with the object you get from the key).

#### Run the AppRouter

```
cd {{ cookiecutter.approuter_module_name }}
npm install # only once
npm start
```

The AppRouter is no ready to serve requests on `http://localhost:5000`.

### Run/Debug the Flask Application

#### Install Dependent Packages
Create a virtual environment and install the dependent packages
```bash
python3 -m venv .venv
pip install -r {{ cookiecutter.python_module_name }}/requirements.txt
source .venv/bin/activate
```

#### Set Environment Variables
To function correctly, the `xssec` library needs the same environment variables as it finds in the Cloud Foundry container. 

You can get these variables with `cf env {{ cookiecutter.scp_app_name }}-core`.

In the output you will find two environment variables: `VCAP_SERVICES` and `VCAP_APPLICATION`.
Both needs to be set in the environment you run Flask in. If you want to debug the app in your IDE of choice, make sure, that both variables are set in the run configuration (in both cases the complete JSON structure)
_HINT_: Watch out for the last `}` in the output and make sure, that you copy the correct `json` object.

**IMPORTANT**: Make sure, that your Flask app listens on port `4000`. If you want to use a different port, make sure, that you configure the correct one in the `{{cookiecutter.approuter_module_name}}/default-env.json` file.
