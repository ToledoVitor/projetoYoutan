#!/bin/sh

yes | python manage.py makemigrations
yes | python manage.py migrate
yes | python manage.py loaddata categories

python manage.py runserver 127.0.0.1:3000
