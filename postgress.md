# PostgresSQL install and setup

1. make sure you have the current requirements.txt
2. install postgres
3. create user:
    in terminal:
    $ psql
    you should see this prompt:
    #

    next type:
    # CREATE USER sisters;
    # CREATE DATABASE barter OWNER sisters;

4. verify that you can connect to the db:

    \q (to quit from psql)

    on terminal type:
    psql barter sisters

    you should see this prompt:
    barter=>

    in terminal run:
    python manage.py migrate
    python manage.py createsuperuser --username <yourusername>

5. after adding email and password you should be able to start the server, go to localhost:8000/admin and login 
