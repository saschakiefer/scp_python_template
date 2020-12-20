#!/bin/bash

cf delete {{ cookiecutter.scp_app_name }}-core -r
cf delete {{ cookiecutter.scp_app_name }} -r
cf delete-service-key {{ cookiecutter.uaa_service_instance_name }} {{ cookiecutter.uaa_service_instance_name }}-key
cf delete-service {{ cookiecutter.uaa_service_instance_name }}
