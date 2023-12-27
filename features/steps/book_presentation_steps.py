from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@when('enter some test information in the form')
def enter_test_information(context):
    context.app.book_presentation_page.input_fields()

@then('verify the right information is present')
def verify_information_is_present(context):
    context.app.book_presentation_page.verify_information_is_present()

@then('scroll down to bottom')
def scroll_down_to_bottom(context):
    context.app.book_presentation_page.scroll_down()

@then('verify "send request" button is available and clickable')
def verify_send_request_button_available_clickable(context):
    context.app.book_presentation_page.wait_for_button_clickable_available()

@then('Verify “buy a subscription” button is available and clickable')
def verify_subscription_button_available_clickable(context):
    context.app.book_presentation_page.wait_for_subscription_clickable_available()



