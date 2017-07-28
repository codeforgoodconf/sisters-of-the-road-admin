Feature: Search Page
  
    Scenario: Load the barter account search page
        Given I am logged in
        When I visit the main checkout page
        Then I see a search field

    Scenario: Typing in the search field
        When I type in the search field
        Then the search button becomes active

    Scenario: Successful search
        Given I have entered text in the search field
        When I hit the search button
        Then I see a list of matching results

    Scenario: Bad search
        Given I have entered text in the search field
        When I hit the search button
        Then I see a message that no results were found

    Scenario: Clicking on an account
        Given I have a list of search results
        When I hit one one of the list items
        Then I am redirected to the barter action page