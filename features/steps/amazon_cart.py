from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(9)
@when('click on the second product')
def click_first_product(context):
    context.driver.find_element(By. Class, 'a-price').click()
    sleep(2)

@when('store product name Small Computer Desk Small Office Desk 32 Inch Writing Desk')
def get_product_name(context):
    small_computer_desk_small_office_desk_32_inch_writing_desk = context.driver.find_element(By.ID, 'Small Computer Desk Small Office Desk 32 Inch Writing Desk').text


@when('click on add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By. ID, 'add-to-cart-button').click()


@when('open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('verify cart has {expected_count} items(s)')
def verify_cart_count(context, expected_count):
    actual_text = context.driver.find_element(By. ID, 'add-to-cart-button').text
    assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'


@then('verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element('small_computer_desk_small_office_desk_32_inch_writing_desk').text
    assert context.'small_computer_desk_small_office_desk_32_inch_writing_desk'[:35] in actual_name, f'Expected {context.product_name}, but got {small_computer_desk_small_office_desk_32_inch_writing_desk}'

