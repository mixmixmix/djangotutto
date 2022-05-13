Old Django. Yes, we are following
https://docs.djangoproject.com/en/1.8/intro/tutorial01/


```
pyenv local 2.7.18
virtualenv -p python2 dj18
source  dj18/bin/activate


pip install -r requirements.txt


```

What we used:
`django-admin startproject tuttomio` - to create directories

`python manage.py migrate` - to create db based on model

add an app to the project
`python manage.py startapp polls`
add the app in settings
`python manage.py makemigrations polls`
`python manage.py sqlmigrate polls 0001`

and rerun
`python manage.py migrate`
