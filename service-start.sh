#!/bin/bash
set -e

# Activate virtualenv && run serivce

SCRIPTDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd $SCRIPTDIR

VENV=".venv"

# Python 3.11.7 with Window
if [ -d "$VENV/bin" ]; then
    source $VENV/bin/activate
else
    source $VENV/Scripts/activate
fi

export PYTHONDONTWRITEBYTECODE=1

#--
# run for dev
#--
uv run fastapi dev main.py

#--
# run for prod
#--
# uv run fastapi run main.py


#--
# run with uvicorn
#--
# uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

#--
# The issue is that 'fcntl' is not available on windows
#--
# gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000 --workers 1

#--
# uv run with gunicorn
#--
# uv run --with gunicorn gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000 --workers 1

# python -m uvicorn main:app --reload --host=0.0.0.0 --port=8000 --workers 2