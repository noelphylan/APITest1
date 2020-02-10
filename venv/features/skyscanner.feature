Feature: Testing interaction of the Skyscanner api

Scenario: Post a skyscanner query and return a session key

	Given I Set POST skyscanner service api endpoint
	When I Set POST request HEADER
	    And Send a POST HTTP request
	Then I receive valid session Response

Scenario: Retrieve the skyscanner session using the session key

	Given I Set GET skyscanner service api endpoint using the session Key
	When I Set GET request HEADER
	    And Send a GET HTTP request
	Then I receive valid Response
