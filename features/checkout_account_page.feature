Feature: Account Page

    Scenario: Load the barter account page
        Given I am logged in
        When I am on the barter account action page
        Then I see the name of the barter account on the page
        And I see the last time the ate
        And I see the last time they worked
        And I see their credit balance
        And I see a button to buy a meal
        And I see a button to add credit
        And I see a link to return to the search page

    Scenario: Buy a meal screen
        When I hit the "Buy a meal" button
        Then a modal opens
        And there is an amount field
        And the default value in the amount field is $1.25
        And there is a "Use Credit" button

    Scenario: Add credit button
        When I hit the "Add Credit" button
        Then a modal opens

    Scenario: Back to search from barter account
        When I hit the "Back to search" button
        Then I am redirected to the search page

    Scenario: Paying for meals
        Given the buy meals modal is active
        And I have entered <amount>
        When I hit the "Use Credit" button
        Then <amount> is deducted from the barter account balance
        And the date of the meal is saved
        And the modal closes
        And I see the new credit balance
        And I see a note that the data has been saved
