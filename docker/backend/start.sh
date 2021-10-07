#!/bin/bash

service ssh start

mkdir -p logs

gunicorn -b 0.0.0.0:8000 app:app --reload