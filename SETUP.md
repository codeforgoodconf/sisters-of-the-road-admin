# Setup

How to get this project running on your machine. 

## 1. Requirements

1. [Install Git.](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
    Check that it's installed:

      ```sh
      which git
      ```

    That should return a path (e.g., `/usr/local/bin/git`).

2. [Install Python 3.](https://www.python.org/downloads/)
    Check that it's installed:

    ```sh
    which python3
    ```

    That should return a path (e.g., `/usr/local/bin/python3`).

3. [Install Node.js.](https://nodejs.org/en/)
    Check that it's installed:

    ```sh
    node -v
    ```    

## 2. Download the project

1. [Fork this repository.](https://github.com/codeforgoodconf/sisters-of-the-road-admin#fork-destination-box)

2. Clone your fork.

    ```sh
    git clone git@github.com:YOUR_GITHUB_USERNAME/sisters-of-the-road-admin.git
    ```

3. Move into that repository.

    ```sh
    cd sisters-of-the-road-admin
    ```

## 3. Set up the development environment

1. Set up a [Python virtual environment](https://docs.python.org/3/library/venv.html). 
You can name it anything you like, but keep it short, lowercase, without any special characters.
    
    ```sh
    python -m venv myvenv
    ```

2. Activate the virtual environment.

    - On Mac/Linux:
    ```sh
    source myvenv/bin/activate
    ```
    
    - On Windows:
    ```sh
    myvenv\Scripts\activate
    ```

3. Install the Python dependencies.

    ```sh
    pip install -r requirements.txt
    ```

4. Install the Node.js dependencies.

    ```sh
    npm install
    ```

5. This project has different settings files for different environments.
Set the environment variable to the *dev* settings.

    ```sh
    export DJANGO_SETTINGS_MODULE=sistersadmin.settings.dev
    ```
    You will need to do this every time you open a new terminal window or tab.

    If you like you can [create an alias in your bash profile](https://www.digitalocean.com/community/tutorials/an-introduction-to-useful-bash-aliases-and-functions) 
    to set it with a single keyword.

    Check your environment variables by entering `env` in terminal.

6. Run database migrations. This will create the database tables.

    ```
    python manage.py migrate
    ```

7. Create your admin account.

    ```
    python manage.py createsuperuser
    ```

    You'll be prompted for your username (lowercase, no spaces), email address and password. **You will not be able to see what you're typing.** Just type it in and hit enter to continue. Save the information. 
    You'll need to remember it to log in.

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
