# Create the virtual environment for python development
python3 -m venv env

# Activate the virtual environment
# Don't forget to change the interpreter (VS Code right bottom)
source env/bin/activate

# Install all project requirements
pip install -r requirements.txt

# Start make migrate
python manage.py makemigrations

# Start the migrate
python manage.py migrate

# Build the static assets folder
python manage.py collectstatic --noinput

# Only use this for the first time (When the database is empty)
# python manage.py createsuperuser --noinput