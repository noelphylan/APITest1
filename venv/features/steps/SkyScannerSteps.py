import json

import requests

from behave import *

@given('I Set POST skyscanner service api endpoint')
def step_impl(context):
    uri = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0";
    context.uri = uri

@given('I Set GET skyscanner service api endpoint')
def step_impl(context):
    uri = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/%7B" + context.sessionKey + "%7D"

    context.uri = uri


@when('I Set POST request HEADER')
def step_impl(context):
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "ea278fe431msh087b44e84f33849p1b9677jsnea2b4c6cd4b8",
        'content-type': "application/x-www-form-urlencoded"
    }
    context.headers = headers

@when('I Set GET request HEADER')
def step_impl(context):
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "ea278fe431msh087b44e84f33849p1b9677jsnea2b4c6cd4b8"
    }
    context.headers = headers

@when('Send a POST HTTP request')
def step_impl(context):
    payload = "inboundDate=2020-09-10&cabinClass=business&children=0&infants=0&country=US&currency=USD&locale=en-US&originPlace=SFO-sky&destinationPlace=LHR-sky&outboundDate=2020-09-01&adults=1"
    response = requests.request("POST", context.uri, data=payload, headers=context.headers, verify=False)
    context.response = response

@when('Send a GET HTTP request using the session Key')
def step_impl(context):
    querystring = {"pageIndex": "0", "pageSize": "10"}
    # print(response.text)
    response = requests.request("GET", context.uri, headers=context.headers, params=querystring, verify=False)


@then('I receive valid session Response')
def step_impl(context):
    print(context.response.status_code)

    location = context.response.headers['location']
    sessionKey = (location[64:])
    context.sessionKey = sessionKey
    assert context.sessionKey is not None

@then('I receive valid Response')
def step_impl(context):
    print(context.response.status_code)
    assert context.response is not None