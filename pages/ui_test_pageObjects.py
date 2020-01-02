from locators.home_page import home_page_locators
from utils.actions import action_elements

author = 'surya pulakhandam'


class home_pageObjects(action_elements):
    url = "http://the-internet.herokuapp.com/dynamic_controls"

    def clicking_remove_checkbox(self):
        self.click_by_xpath(home_page_locators.remove_button)

    def check_for_checkbox(self):
        self.check_element_visible_id(home_page_locators.checkbox)

    def clicking_add(self):
        self.click_by_xpath(home_page_locators.remove_button)

    def check_for_added_message(self):
        self.check_text_by_id(home_page_locators.message, home_page_locators.added_message)

    def check_for_remove_message(self):
        self.check_text_by_id(home_page_locators.message, home_page_locators.remove_message)

    def check_enable_button_default_state(self):
        self.check_text_by_xpath(home_page_locators.enable_button, home_page_locators.enable_state)

    def click_enable_button(self):
        self.click_by_xpath(home_page_locators.enable_button)

    def check_disable_button_state(self):
        print(home_page_locators.enable_button)
        print(home_page_locators.disable_state)
        self.check_text_by_id(home_page_locators.message, home_page_locators.disabled_text_message)

    def check_enable_button_state(self):
        self.check_text_by_id(home_page_locators.message, home_page_locators.enabled_text_message)