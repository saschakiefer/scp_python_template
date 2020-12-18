# {{cookiecutter.project_name}}

Simple SAP Cloud Platform PaaS Flask App with AppRouter protection

## Prerequisites

Create Service
```bash
cf create-service xsuaa application {{ cookiecutter.uaa_service_instance_name }} -c xs-security.json
```

## Post Deployment

Add Role
