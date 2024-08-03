#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput


gunicorn sxj_quiz.wsgi:application