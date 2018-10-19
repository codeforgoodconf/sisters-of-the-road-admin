# Setup

How to get this project running on your machine. 

## 1. Requirements

1. [Install Git.](https://git-scm.com/downloads)
    Check that it's installed:

      ```bash
      which git
      ```

    That should return a path (e.g., `/usr/local/bin/git`).

2. [Install Python 3.](https://www.python.org/downloads/)
    Mac users follow [this guide](BREW_PYENV_NODE_SETUP.md).
    Check that it's installed:

    ```bash
    which python3
    ```

    That should return a path (e.g., `/usr/local/bin/python3`).

3. [Install Node.js.](https://nodejs.org/en/)
    Check that it's installed:

    ```bash
    node -v
    ```    

## 2. Download the project

1. Fork this repository. [Help](https://help.github.com/articles/fork-a-repo/)

2. Clone your fork.

    ```bash
    git clone https://github.com/YOUR_GITHUB_USERNAME/sisters-of-the-road-admin.git
    ```

3. Move into that repository.

    ```bash
    cd sisters-of-the-road-admin
    ```

## 3. Set up the development environment

1. Set up your python environment
    1. Follow [these instructions](PIPENV_SETUP.md) to use pipenv (recommended).
    2. Follow [these instructions](VENV_SETUP.md) to use venv

4. Install the Node.js dependencies.

    ```bash
    npm install
    ```

5. If you are **not** using Pipenv: This project has different settings files for different environments.
Set the environment variable to the *dev* settings.

    ```bash
    export DJANGO_SETTINGS_MODULE=sistersadmin.settings.dev
    ```
    
    Unless you are using pipenv, you will need to do this every time you open a new terminal window or tab.

    If you like you can [create an alias in your bash profile](https://www.digitalocean.com/community/tutorials/an-introduction-to-useful-bash-aliases-and-functions) to set it with a single keyword.

    Check your environment variables by entering `env` in terminal.

6. Run database migrations. This will create the database tables.

    ```bash
    python manage.py migrate
    ```

7. Create your admin account.

    ```bash
    python manage.py createsuperuser
    ```

    You'll be prompted for your username (lowercase, no spaces), email address and password. **You will not be able to see what you're typing.** Just type it in and hit enter to continue. Save the information. You'll need to remember it to log in.

8. Run Webpack to compile the JavaScript files.

    ```bash
    ./node_modules/webpack/bin/webpack.js --config webpack.config.js
    ```

    You will need to do this every time you make changes to the JavaScript files. You can create another bash profile alias to make this easier.

## 4. Run the app

- Start the server.
    ```sh
    python manage.py runserver
    ```

    The app will now be running in your browser at http://localhost:8000/.

    The admin dashboard is available at http://localhost:8000/admin.

    You should be able to log in to admin with the account you created in step 7 above.

---

Refer to the [Django Girls Tutorial](https://tutorial.djangogirls.org/en/installation/) if you need more details 
for your particular machine.

If you are still unable to get the app running, please [open a new issue](https://github.com/codeforgoodconf/sisters-of-the-road-admin/issues/new) describing what went wrong.
