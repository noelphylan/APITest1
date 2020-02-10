import requests
from behave import given, when, then

"""@given('we have behave installed')
def step_impl(context):
    pass
"""
#resp = None

@when('we perform a get request on the open api')
def step_impl(context):
    print(requests.get('http://api.open-notify.org/astros.json/'))
    context.resp = requests.get('http://api.open-notify.org/astros.json/')

@then('the number of astronauts in space are returned')
def step_impl(context):
    if context.resp is not None:
        print(context.resp.json())

        assert context.failed is False
        print ('we are finished pass')
    else:
        print('we are finished fail')
        print (context.resp)
        assert context.failed is True