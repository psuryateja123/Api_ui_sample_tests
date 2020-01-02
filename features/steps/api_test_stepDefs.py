import http
from urllib import response
import json
import requests
from behave import given, then
from nose.tools import assert_true
from requests.structures import CaseInsensitiveDict

from utils.actions import action_elements

author = 'surya pulakhandam'
import logging

logging.basicConfig(level=logging.INFO)
#logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(message)s')

@given(u'I post the api')
def api_post(self):
    api_url = 'http://dummydecisionapi.azurewebsites.net/decision'
    with open('application.json') as f:
        payload = json.load(f)

    response = requests.post(api_url, json=payload)

    logging.info(response.json())
    logging.warning(response.json())
    logging.error(response.json())
    logging.critical(response.json())
    api_response = response.json()
    print(response. headers)
    return response.headers

@then(u'I check for result')
def step_impl(context):
    logging.info(api_post)
    print(api_post)



