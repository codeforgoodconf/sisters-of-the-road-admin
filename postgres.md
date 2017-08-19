# PostgresSQL install and setup

1. Make sure you have the current requirements.txt
    pip install -r requirements.txt
2. Install postgres
3. Create user:
    in terminal:
    
        $ psql
        
    you should see this prompt:
        
        #

    next type:
    
        # CREATE USER sisters;
        # CREATE DATABASE barter OWNER sisters;

4. Verify that you can connect to the db:

    `\q` (to quit from psql)

    on terminal type:
    
        psql barter sisters

    you should see this prompt:
    
        barter=>

5. Make any database migrations 
    Navigate to the root directorty of the django project
    Then run:
    
        python3 manage.py migrate
        python3 manage.py createsuperuser --username <yourusername>

6. You'll be prompted for an email address and password, and then you should be able to start the server:

        python3 manage.py runserver
        
    go to `localhost:8000/admin` and login!
