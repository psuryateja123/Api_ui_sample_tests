import json
import requests
from behave import given, then

author = 'surya pulakhandam'
import logging

logging.basicConfig(level=logging.INFO)
#logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(message)s')
api_url = 'http://dummydecisionapi.azurewebsites.net/decision'

@given(u'I post the api with John smith json file')
def api_john_post(self):
    with open('john.json') as f:
        payload = json.load(f)

    response = requests.post(api_url, json=payload)

    logging.info(response.json())
    logging.warning(response.json())
    logging.error(response.json())
    logging.critical(response.json())
    api_response = response.json()
    print(response.headers)
    return response.headers

@then(u'I print the John smith result')
def step_impl(context):
    logging.info(api_john_post)
    print(api_john_post)


@given(u'I post the api with Karen Jones json file')
def api_karen_post(self):
    with open('karen.json') as f:
        payload = json.load(f)

    response_karen = requests.post(api_url, json=payload)

    logging.info(response_karen.json())
    logging.warning(response_karen.json())
    logging.error(response_karen.json())
    logging.critical(response_karen.json())
    api_response = response_karen.json()
    print(response_karen.headers)
    return response_karen.headers

@then(u'I print Karen Jones results')
def step_impl(context):
    logging.info(api_karen_post)
    print(api_karen_post)