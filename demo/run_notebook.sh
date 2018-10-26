#!/bin/bash
set -e
# jupyter-notebook --ip=0.0.0.0 --allow-root --port 8888
python manage.py shell_plus --notebook
