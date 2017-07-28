Feature: Barter Account Name Search

    Scenario: Searching
        When I submit search form
        Then I see a list of search matches

    Scenario: Exact Match
        Given I know an exact name
        When I submit search form
        Then the exact match is at the top of the search results