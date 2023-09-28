from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ORDERS_BTN = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()

@when('Search for {product}')
def search_on_amazon(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_product(product)


@when('Click Orders')
def click_orders(context):
    # context.driver.find_element(*ORDERS_BTN).click()
    context.app.header.click_orders()

@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGNIN_BTN),
        message='SignIn btn from popup not clickable'
    ).click()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
