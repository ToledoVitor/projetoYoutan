#!/bin/sh

yes | python manage.py makemigrations
yes | python manage.py migrate
yes | python manage.py loaddata categories

python manage.py runserver 0.0.0.0:3000
