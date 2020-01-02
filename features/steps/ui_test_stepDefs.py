from behave import given, then
from pages.ui_test_pageObjects import home_pageObjects

author = 'surya pulakhandam'


@given(u'I navigate to test page')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.navigate()


@then(u'I check for checkbox')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.check_for_checkbox()


@then(u'I click Remove button')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.clicking_remove_checkbox()


@then(u'the checkbox should disappear')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.check_for_checkbox()
    home_page.check_for_remove_message()


@then(u'I click add button')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.clicking_add()


@then(u'the checkox should reappear')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.check_for_added_message()

@then(u'I check the text field status')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.check_enable_button_default_state()


@then(u'I click on enable button')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.click_enable_button()


@then(u'I check the status')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.check_disable_button_state()

@then(u'I check the current status')
def step_impl(context):
    home_page = home_pageObjects(context.browser)
    home_page.check_enable_button_state()


