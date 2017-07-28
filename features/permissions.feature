Feature: Permission system and logins

    Scenario: checkout user logging in
        Given I am a checkout user
        When I submit login form with valid credentials
        Then I am redirected to the checkout page

    Scenario: admin user login
        Given I am an admin user
        When I submit login form with valid credentials
        Then I am redirected to the checkout page

    Scenario: bad login
        When I submit login form with invalid credentials
        Then I am redirected to the login page
        And I see and error message