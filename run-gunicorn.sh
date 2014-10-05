#!/bin/bash

PROJECT_NAME="money"
VERBOSE_NAME="home_accountancy"

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$BASE_DIR/venv/"
PROJECT_DIR="$BASE_DIR/money/"

PID_FILE="$BASE_DIR/$PROJECT_NAME.pid"
SOCK_FILE="$BASE_DIR/$PROJECT_NAME.sock"
LOG_FILE="$BASE_DIR/$PROJECT_NAME.log"

if [ -f "$PID_FILE" ]; then rm "$PID_FILE"; fi

# enable venv
. "$VENV_DIR/bin/activate"

# start gunicorn
cd "$PROJECT_DIR"
exec gunicorn "$PROJECT_NAME.wsgi:application" \
  --env="DJANGO_SETTINGS_MODULE=money.settings.production" \
  --name="$VERBOSE_NAME" \
  --workers=3 \
  --bind="unix:$SOCK_FILE" \
  --pid="$PID_FILE" \
  --log-file="$LOG_FILE" \
  --log-level=warning

