# Setup steps

## Laptop environment

* Make sure you have Python 3 installed
```
$ which python3
```
* Make sure you have git installed
```
$ which git
```

## Get the team repository and make it your working directory

```
$ git clone git@github.com:codeforgoodconf/sisters-of-the-road-admin.git
$ cd sisters-of-the-road-admin
```

## Set up a Python [virtual environment](https://docs.python.org/3/library/venv.html)

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Set up for [React](https://en.wikipedia.org/wiki/React_(JavaScript_library))

```
$ npm install
$ ./node_modules/.bin/webpack --config webpack.config.js
```

## Try to run the app

```
$ python manage.py runserver
```

Make sure you can load the default Django page ("It worked!")


## Try to run the tests

```
$ python manage.py behave
```

You should see a lot of `NotImplementedError`.

If at any point these steps don't work for you, feel free to open an issue explaining the problem you ran into!
