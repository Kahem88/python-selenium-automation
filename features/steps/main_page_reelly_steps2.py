from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given('Open the reelly main page')
def open_reelly_page2(context):
    context.app.main_page_reelly2.open_reelly_page()

@when('Log in to the reelly page')
def log_into_the_page(context):
    context.app.main_page_reelly2.log_in()
    sleep(2)

@when('click on connect the company')
def click_connect_company_button(context):
    context.app.main_page_reelly2.click_connect_page()

@when('switch the new tab')
def switch_to_new_window(context):
    context.app.main_page_reelly2.switch_to_new_window()

