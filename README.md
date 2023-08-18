# Env and Docker dont work due to KERNAL32.dll error at my PC

# Install all required dependencies from requirements.txt, especially:
    python -m pip install Django
    pip install -U djoser
    pip install -U djangorestframework_simplejwt
    pip install -U pytest
    pip install -U psycopg2
    pip install -U pytest-django
    pip install -U responses

# Commands to creatre migrationg with db
cd restaurant_api
python manage.py migrate
python manage.py makemigrations

# Creating superuser
python manage.py createsuperuser
username: root
email: root@root.com
password: root
password2: root

# Command to run server
python manage.py runserver
