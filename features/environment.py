from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from app.application import Application

# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/connect_the_company.feature


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
#     # driver_path = ChromeDriverManager(version="119.0.5994.0").install()  # Replace with the exact version you downloaded
    driver_path = '/Users/kahempatrick/QA/python-selenium-automation/chromedriver'
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
#     # context.driver = webdriver.Chrome()
#
#     ### OTHER BROWSERS ###
#     # service = FirefoxService(executable_path='')
#     # options = webdriver.FirefoxOptions()
#     # context.driver = webdriver.Firefox(options=options)
#     # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # driver_path = '/Users/kahempatrick/QA/python-selenium-automation/chromedriver'
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'kahempatrick_KhZkbM'
    # bs_key = 'v2pDquqNzPnFxWnWfZxb'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '11',
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
    context.driver.set_window_size(1280, 720)

    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()