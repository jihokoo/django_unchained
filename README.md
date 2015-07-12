### django_unchained

#### instructions:

- download vagrant and ansible
- `vagrant up`
- `vagrant ssh`
- `cd /var/www/django-app`
- `source bin/activate`
- `cd django_unchained`
- `python manage.py runserver 0.0.0.0:7000`
- navigate to localhost:7000

#### apps:

- utilities
  * houses services and models

- webapp
  * starts at localhost:7000/factory
  * basic webapp with crud functionality
  * consumes factory service from utilities

- api
  * starts at localhost:7000/api/factory
  * consumes factory service from utilities
