
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

author = 'surya pulakhandam'


def before_all(context):
    print('browser started')
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

    chrome_options = Options()
    # incognito window
    chrome_options.add_argument("--incognito")

def after_all(context):
    context.browser.quit()
