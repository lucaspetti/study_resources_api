# Study Resources API

A Django app using the Rest Framework made to retrieve and manage data for an online profile.

### Setup

Python version: 3.6.9

Django version: 3.0.6

### Running the app

Make sure you have python and Django installed on your machine, then run the migrations:

`python manage.py makemigrations`

`python manage.py migrate`

To serve the app:

`python manage.py runserver`

You may want to create a super user, or admin user. To do that just run:

`python manage.py createsuperuser`

And enter the desired username and password.

#### Tests

To run the test suite:

`python manage.py test`

#### Fixtures

There are files with fixtures for CS subjects and example resources. You can edit the data there and populate the database running:

`python manage.py loaddata resources.json`
