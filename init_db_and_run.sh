#!/usr/bin/env bash
python manage.py makemigrations
python manage.py migrate

# creates admin with password 'adminpass'
echo "from django.contrib.auth.models import User;"\
 "User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell
python manage.py runserver 8000