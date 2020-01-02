import json

import requests
from selenium.common.exceptions import NoSuchElementException

author = 'surya pulakhandam'



from selenium.webdriver.common.by import By

class action_elements(object):

    def __init__(self, driver):
        self.driver = driver

    def navigate(self):
        self.driver.get(self.url)

    def click_by_id(self, element_id):
        element = self.driver.find_element_by_id(element_id)
        return element

    def click_by_xpath(self, xpath):
        element_xpath = self.driver.find_element_by_xpath(xpath)
        element_xpath.click()

    def check_element_visible_id(self, element):
        try:
            self.driver.find_element_by_id(element)
        except NoSuchElementException:
            return False
        return True

    def check_text_by_id(self, element_id, text_to_check):
        element = self.driver.find_element_by_id(element_id).text
        assert element == text_to_check

    def check_text_by_xpath(self, element_xpath, default_button_status):
        element_to_check = self.driver.find_element_by_xpath(element_xpath).text
        assert element_to_check == default_button_status

    def post_api(self, json_file):
        task = {"summary": "decision", "description": "Declined|Accepted"}
        resp = requests.post('http://dummydecisionapi.azurewebsites.net/decision',
                             data=json.dumps(task),
                             headers={'Content-Type': json_file + '/json'})
        return resp
