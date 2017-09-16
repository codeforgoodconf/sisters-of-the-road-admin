# Setup

How to get this project running on your machine.

## 1. Requirements

1. [Install Git.](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

  Check that it's installed:

    ```
    which git
    ```

    That should return a path (e.g., `/usr/local/bin/git`).

1. Install Python 3. You have a few options:

  - Using a downloadable installer for any operating system: https://www.python.org/downloads/

  - With [Homebrew](https://brew.sh/) for macOS:

      ```sh
      brew install python3
      ```

  - With [Scoop](http://scoop.sh/) for Windows:

      ```sh
      scoop install python3
      ```

  - Once installed, check that it's installed:

      ```sh
      which python3
      ```

      That should return a path (e.g., `/usr/local/bin/python3`).

1. Install PostgreSQL.

  - With [Postgres.app](https://postgresapp.com/) for macOS.

  - With [BigSQL](https://www.openscg.com/bigsql/postgresql/installers.jsp/) for Windows.

  - Other [options are available](https://www.postgresql.org/download/).

  <!-- Any of the interactive/graphical installer options (e.g., EnterpriseDB or BigSQL) will work just fine.

  While running the installer you will be prompted to choose a password for the default `postgres` user. Use `admin`.
 -->
  Once that's downloaded and installed, check that it's installed:

    ```sh
    which postgres
    ```

    That should return a path (e.g., `/usr/local/bin/postgres`).

1. [Install Node.js.](https://nodejs.org/en/)

## 2. Download the project.

1. Fork this repository.

1. Clone git repository and move into that.

    ```sh
    git clone git@github.com:YOUR_GITHUB_USERNAME/sisters-of-the-road-admin.git
    ```

1. Move into that repository.

    ```sh
    cd sisters-of-the-road-admin
    ```

## 3. Set up development environment:

1. Set up a [Python virtual environment](https://docs.python.org/3/library/venv.html):

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

1. Install Node.js dependencies.

    ```sh
    npm install
    webpack --config webpack.config.js
    ```

1. Setup PostgreSQL database.

    - Create a user:

        ```sh
        psql
        ```

        You will be asked for your password. If you used the password 'admin' for the default `postgres` user when installing PostgreSQL, then enter 'admin' here.

    - That will open up the PostgreSQL prompt. Create the database:

        ```sh
        CREATE USER sisters;
        CREATE DATABASE barter OWNER sisters;
        ```

    - Exit the `psql` prompt:

        ```sh
        \q
        ```

    - Verify that you can connect to the database:

        ```
        psql barter sisters
        ```

        That should enter you into the PostgreSQL prompt again.

        Exit the prompt by entering `\q` and hitting <kbd>Enter</kbd>.

    - Run database migrations.

        ```
        python3 manage.py migrate
        python3 manage.py createsuperuser --username [YOUR USERNAME]
        ```

        Replace `[YOUR USERNAME]` with your desired username (e.g., `kjohnson`).

        You'll be prompted to create a user with your email address and password. Do so, and save the information. You'll need to remember it to log in.

## 4. Run the app.

1. Run:

    ```sh
    python manage.py runserver
    ```

    The app will now be running in your browser at [http://localhost:8000/].

    The admin dashboard is available at [http://localhost:8000/admin].


## 5. Run the tests.

1. First, stop the running app with <kb>Ctrl</kbd>+<kbd>c</kbd>.

1. Run tests:

    ```sh
    python manage.py behave
    ```

    That should output a lot of `NotImplementedError`s.

---

If you have trouble with any of these steps, please [open a new issue](/codeforgoodconf/sisters-of-the-road-admin/issues/new) describing what went wrong.
