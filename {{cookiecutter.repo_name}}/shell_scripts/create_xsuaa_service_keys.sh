#!/bin/bash

cf create-service-key {{ cookiecutter.uaa_service_instance_name }} {{ cookiecutter.uaa_service_instance_name }}-key
cf service-key {{ cookiecutter.uaa_service_instance_name }} {{ cookiecutter.uaa_service_instance_name }}-key
