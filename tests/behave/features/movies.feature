@movies
Feature: Movies API

  @get-movies
  Scenario: Get all movies
    When I request all movies
    Then the response status should be 200
    And the response should contain the following movies:
      | name             |
      | Central Station  |
      | Bacurau          |
      | City of God      |
      | A Dog's Will     |

  Scenario: Get a movie by ID
    When I request movie with id 12345678-9012-3456-7890-1234567890e1
    Then the response status should be 200
    And the response should contain:
      | key          | value             |
      | name         | Central Station   |

  Scenario: Get a movie by not exists ID
    When I request movie with id 22345678-9012-3456-7890-1234567890e1
    Then the response status should be 404

    Scenario: Create a new movie
    When I create a movie with:
      | key          | value             |
      | name         | I'm Still Here    |
    Then the response status should be 201

  Scenario: Update a movie
    When I update movie with id 12345678-9012-3456-7890-1234567890e1 with:
      | key          | value             |
      | name         | Central do Brasil |
    Then the response status should be 200
    And the response should contain:
      | key          | value             |
      | name         | Central do Brasil |

  Scenario: Update a non exists movie
    When I update movie with id 22345678-9012-3456-7890-1234567890e1 with:
      | key          | value             |
      | name         | Central do Brasil |
    Then the response status should be 404

  Scenario: Delete a movie
    When I delete movie with id 12345678-9012-3456-7890-1234567890e1
    Then the response status should be 204

  Scenario: Delete non exists movie
    When I delete movie with id 22345678-9012-3456-7890-1234567890e1
    Then the response status should be 404