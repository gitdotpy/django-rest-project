#!/bin/bash

####USE THIS IN PRODUCTION WEB SERVER####
# Collect static files 
#echo "Collect static files"
#python manage.py collectstatic --noinput
#########################################

# Make database migrations
echo "Apply database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create SuperUser
echo "Creating Superuser"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password')"

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000