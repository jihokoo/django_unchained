## django_unchained

### apps:

##### utilities
- houses services and models

##### webapp
- starts at localhost:7000/factory
- basic webapp with crud functionality
- consumes factory service from utilities
- endpoints:
  - ShowAllView (GET:/factory)
  - CreateView (GET:/factory/create)
  - Create (POST:/factory/create)
  - ShowOneView (GET:/factory/<factory_id>)
  - UpdateView (GET:/factory/<factory_id>/update)
  - Update (POST:/factory/<factory_id>/update)
  - Delete (POST:/factory/<factory_id>/delete)

##### api
- starts at localhost:7000/api/factory
- consumes factory service from utilities
- endpoints:
  - GetAll (GET:/api/factory)
  - Create (POST:/api/factory)
  - GetOne (GET:/api/factory/<factory_id>)
  - Update (UPDATE:/api/factory/<factory_id>)
  - Delete (DELETE:/api/factory/<factory_id>)

### dependencies:

- Django
- psycopg2
- django-jsonview


### instructions:

- download vagrant and ansible
- `vagrant up`
- `vagrant ssh`
- `cd /var/www/django-app`
- `source bin/activate`
- `cd django_unchained`
- run tests: `python manage.py test`
- run server: `python manage.py runserver 0.0.0.0:7000`
- navigate to localhost:7000
