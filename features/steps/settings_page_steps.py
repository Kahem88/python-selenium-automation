from behave import given, when, then
from selenium.webdriver.common.by import By


@when ('Click on Subscription & payments option.')
def click_subscription_and_payments(context):
    context.app.settings_page.click_subscription_and_payments()
@when ('Verify the right page opens.')
def verify_right_page_opens(context):
    context.app.settings_page.verify_right_page_opens()
    # expected_url = 'https://soft.reelly.io/subscription'
    # actual_url = context.driver.actual_url
    # assert actual_url == expected_url, f'Expected {expected_url} but got {actual_url}'

    actual_url = 'https://soft.reelly.io/subscription'
