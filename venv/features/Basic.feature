Feature: Testing an open API with no access key required

Scenario: Perfrom a get request on an open api
    #Given we have behave installed
    When we perform a get request on the open api
    Then the number of astronauts in space are returned