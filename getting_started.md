# Setup steps

## laptop environment

* make sure you have python3 installed
* make sure you have git installed


## get the team repository

```
$ git clone git@github.com:codeforgoodconf/sisters-of-the-road-admin.git
$ cd sisters-of-the-road-admin
```

## setup a virtualenv

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## try to run the app

```
$ python manage.py runserver
```

    Make sure you can load the default django page


## try to run the tests

```
$ python manage.py behave
```
    You should get a lot of NotImplementedError