#!/usr/bin/env bash

if [ ! -d ./venv ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt

python -m main 'Приложение_к_заданию_бек_разработчика.xlsx'

deactivate