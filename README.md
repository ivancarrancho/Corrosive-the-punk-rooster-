# Corrosive-the-punk-rooster-

## Start the project

Really, we don't know about the reason of the project

## Axes
	$ pip install django-axes

	$ PYTHONPATH=$PYTHONPATH:$PWD django-admin.py test axes --settings=axes.test_settings

## Configuration

First of all, you must add this project to your list of INSTALLED_APPS in settings.py:

		INSTALLED_APPS = (
		    'django.contrib.admin',
		    'django.contrib.auth',
		    'django.contrib.contenttypes',
		    'django.contrib.sessions',
		    'django.contrib.sites',
		    ...
		    'axes',
		    ...
)
Next, install the FailedLoginMiddleware middleware:

		MIDDLEWARE_CLASSES = (
		    'django.middleware.common.CommonMiddleware',
		    'django.contrib.sessions.middleware.SessionMiddleware',
		    'django.contrib.auth.middleware.AuthenticationMiddleware',
		    'axes.middleware.FailedLoginMiddleware'
		)
