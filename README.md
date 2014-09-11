home_accountancy
================

## Initial setup:
* Create virtualenv in some folder, e.g. **venv**: `virtualenv venv`
* Switch to venv: `source venv/bin/activate`
* Install pip requirements: `pip install -r requirements.txt`
* Make migrations for taggit: `./money/manage.py makemigrations taggit`
* Migrate django db: `./money/manage.py migrate`
* Collect django static files: `./money/manage.py collectstatic`
* Create superuser: `./money/manage.py createsuperuser`
* Enjoy django!
