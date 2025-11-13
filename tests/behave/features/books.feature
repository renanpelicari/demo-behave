Feature: Books API

  Scenario: Get all books
    When I request all books
    Then the response status should be 200
    And the response should contain the following books:
      | name                  |
      | Dom Casmurro          |
      | Barren Lives          |
      | Captains of the Sands |