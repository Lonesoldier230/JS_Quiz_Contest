#!/bin/bash
python manage.py makemigrations
python manage.py migrate


gunicorn sxj_quiz.wsgi:application --bind 0.0.0.0:8000