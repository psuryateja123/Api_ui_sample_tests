
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



# from selenium import webdriver
# from browserstack.local import Local
# import os, json
#
# CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'browserstackConfig.json'
# TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
#
# with open(CONFIG_FILE) as data_file:
#     CONFIG = json.load(data_file)
#
# bs_local = None
#
# BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['user']
# BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['key']
#
# def start_local():
#     """Code to start browserstack local before start of test."""
#     global bs_local
#     bs_local = Local()
#     bs_local_args = { "key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true" }
#     bs_local.start(**bs_local_args)
#
# def stop_local():
#     """Code to stop browserstack local after end of test."""
#     global bs_local
#     if bs_local is not None:
#         bs_local.stop()
#
#
# def before_feature(context, feature):
#     desired_capabilities = CONFIG['environments'][TASK_ID]
#
#     for key in CONFIG["capabilities"]:
#         if key not in desired_capabilities:
#             desired_capabilities[key] = CONFIG["capabilities"][key]
#
#     if 'BROWSERSTACK_APP_ID' in os.environ:
#         desired_capabilities['app'] = os.environ['BROWSERSTACK_APP_ID']
#
#     if "browserstack.local" in desired_capabilities and desired_capabilities["browserstack.local"]:
#         start_local()
#
#     context.browser = webdriver.Remote(
#         desired_capabilities=desired_capabilities,
#         command_executor="http://%s:%s@%s/wd/hub" % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY, CONFIG['server'])
#     )
#
# def after_feature(context, feature):
#     context.browser.quit()
#     stop_local()
