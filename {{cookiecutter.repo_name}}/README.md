# {{cookiecutter.project_name}}

Simple SAP Cloud Platform PaaS App. Written in Python with Flask and protected by the AppRouter.

## Prerequisites
You have to be logged in to your cloud platform service account.

Before you can deploy the application, you have to create a `xsuaa` service instance with
```bash
cf create-service xsuaa application {{ cookiecutter.uaa_service_instance_name }} -c xs-security.json
```

## Post Deployment

After the deployment you have to create a Role Collection which contains the `User`-role (alternatively you cann add the role to an existing role collection).
This role collection needs to be assigned to the user to logon.
