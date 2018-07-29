#Installing and Using pipenv

[Pipenv](https://docs.pipenv.org/) is the officially recommended way to manage a python environment. There are many advantages over using `venv` and a `requirements.txt`:

* Automatic creation and management of python environments
* Automatic adding and removing of packages from the `Pipfile` (the file that keeps track of requirements)
* Identification of conflicting requirements in all modules and sub-modules
* Generation of a `Pipfile.lock` to produce deterministic builds
* Automatic injection of environment variables

## Installation

Once you have installed python3 (if you have a Mac [using brew and pyenv](BREW_PYENV_NODE_SETUP.md) on a Mac, maybe your Linux package manager, or by downloading it on Windows) you can install `pipenv` by doing this

```bash
pip3 install -U pip setuptools pipenv
```

## Installing your virtualenv using pipenv

Do this:

```bash
pipenv --python 3.6.5
pipenv install --dev
```

Once these processes are done, you have a virtualenv with the requirements installed. You can find the location of this virtual environment py doing this:

```bash
pipenv --venv
```

## Automatic loading of environment variables

We have a key/value pair that must be loaded into our environment to run this locally. Create a file named `.env` with this line:

```
DJANGO_SETTINGS_MODULE=sistersadmin.settings.dev
```

Now, whenever you do `pipenv shell` or `pipenv run` the environment will be automatically loaded with that key/value pair.
