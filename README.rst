When your salesforce-django connection isn't working in any of your projects, try this
"connection only" app.

***Usage***::

pipenv install

Change the settings in settings.py::

  pipenv manage.py shell
  from mysite.models import Recordtype
  x = Recordtype.objects.all().count()
  if x > 0:
    print('Connection is working.')
