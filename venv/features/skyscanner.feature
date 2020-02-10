Feature: Testing interaction of the Skyscanner api

Scenario: skyscanner session

	Given I Set POST skyscanner service api endpoint
	When I Set POST request HEADER
	    And Send a POST HTTP request
	Then I receive valid session Response

	Given I Set GET skyscanner service api endpoint
	When I Set GET request HEADER
	    And Send a GET HTTP request
	Then I receive valid Response