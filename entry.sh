#!/bin/bash

echo "Run back"
sleep 10

python manage.py migrate
python manage.py runserver 7000