import json

import requests

def createSkyScannerSession():
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"

    payload = "inboundDate=2020-09-10&cabinClass=business&children=0&infants=0&country=US&currency=USD&locale=en-US&originPlace=SFO-sky&destinationPlace=LHR-sky&outboundDate=2020-09-01&adults=1"
    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "ea278fe431msh087b44e84f33849p1b9677jsnea2b4c6cd4b8",
        'content-type': "application/x-www-form-urlencoded"
    }

    """response = requests.request("POST", url, data=payload, headers=headers)

    print(response.status_code)

    #responseHeader = json.loads(response.headers)

    print(response.headers['location'])

    location = response.headers['location']

    sessionKey = (location[64:])"""

    sessionKey = "noel"
    print (sessionKey)

    #parsed_json = (json.loads(json_data))
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))

    #print(response.text)

    return sessionKey

def pollSkyScannerSession(sessionKey):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/%7B"+sessionKey+"%7D"

    querystring = {"pageIndex": "0", "pageSize": "10"}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "ea278fe431msh087b44e84f33849p1b9677jsnea2b4c6cd4b8"
    }

    # print(response.text)
    #response = requests.request("GET", url, headers=headers, params=querystring)

    print(sessionKey)

if __name__ == '__main__':
    sessionKey = createSkyScannerSession()
    pollSkyScannerSession(sessionKey)
