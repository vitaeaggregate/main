# Django Project Setup and Deployment

## Overview

This project is a Django application configured for development and deployment. It includes setup for PostgreSQL, Python virtual environments, and deployment on Vercel.

## Prerequisites

- [PostgreSQL](https://www.postgresql.org/)
- [Python 3.x](https://www.python.org/)
- [Vercel CLI](https://vercel.com/docs/concepts/deployments/overview)

## Setup

### 1. Configure PostgreSQL

1. Access the PostgreSQL container:
   ```bash
   su postgres
   ```

2. Start `psql`:
   ```bash
   psql
   ```

3. Create a new database named "malenia":
   ```sql
   CREATE DATABASE malenia;
   ```

### 2. Set Up Python Environment

1. Create a Python virtual environment:
   ```bash
   python3 -m venv env
   ```

2. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```

3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Initialize Django Project

1. Start a new Django project named "api":
   ```bash
   django-admin startproject api .
   ```

2. Create a `.env` file in the root directory with the following content:
   ```ini
   DJANGO_SUPERUSER_EMAIL=admin@example.com
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_PASSWORD=admin123
   SECRET_KEY=django-insecure-lrzfi@3@=l430n^%xkiz-k(1p4mg6yh@ggpi^70(je9apm2317
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/malenia
   DEBUG=True
   ```

3. Update `api/settings.py`:
   - Import required modules
   - Update `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `DATABASES` settings
   - Configure static file settings

4. Update `api/urls.py` to include URL routing for static files and default Django landing page.

5. Update `api/wsgi.py` to include `app = application`.

### 4. Run Migrations and Collect Static Files

1. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

2. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser --noinput
   ```

4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

### 5. Configure Vercel Deployment

1. Create `vercel.json` file:
   ```json
   {
     "builds": [
       {
         "src": "api/wsgi.py",
         "use": "@vercel/python"
       },
       {
         "src": "build.sh",
         "use": "@vercel/static-build",
         "config": {
           "distDir": "static-build"
         }
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "api/wsgi.py"
       },
       {
         "src": "/static/(.*)",
         "dest": "/static/$1"
       }
     ]
   }
   ```

2. Create `build.sh` file:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic
   ```

3. Install Vercel CLI:
   ```bash
   npm install vercel
   ```

4. Run Vercel development server:
   ```bash
   npx vercel dev
   ```

## Notes

- Update `.env` settings as needed for production.
- Ensure that Vercel project settings match the configuration specified in `vercel.json`.