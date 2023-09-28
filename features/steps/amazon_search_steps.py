from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


# @given('Open Amazon page')
# def open_amazon(context):
#     context.app.main_page.open_main()
    # sleep(9)



@when('Click Amazon Orders link')
def click_amazon_orders(context):
    # context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.app.find_element(By.ID, 'nav-orders').click()


# @when('Click Orders')
# def click_orders(context):
#     context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify search result is correct')
def verify_search_result(context):
    expected_result = '"table"'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then('Verify sign in page opened')
def verify_signin_page_opened(context):
    expected_text = 'Sign in'
    # actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    # assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
    #
    # context.driver.find_element(By.ID, 'ap_email')

    # context.app.signin_page.verify_signin_page_opened()
    context.app.signin_page.verify_signin_page_opened(expected_text)
