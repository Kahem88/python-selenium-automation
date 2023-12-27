from behave import given, when, then
from selenium.webdriver.common.by import By


# from selenium.webdriver.support import expected_conditions as EC
# from your_page_objects import LoginPage
# import assert

#
# SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_BTN = (By.ID, 'nav-search-submit-button')
# ORDERS_BTN = (By.ID, 'nav-orders')
# FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
# SIGNIN_BTN = (By.CSS_SELECTOR, '.login-button w-button')
# #nav-signin-tooltip .nav-action-signin-button'


@given('Open the main page')
def open_main_page(context):
    context.app.main_page_reelly.open_reelly_signup_page()


#


@when('Log in to the page')
def log_into_the_page(context):
    context.app.log_in.sign_in()


@when('Click on settings option.')
def click_settings_option(context):
    # context.app.find_element(By.CSS_SELECTOR, 'menu-button-text').click()
    context.app.main_page_reelly.click(By.XPATH, "//a[contains(@href, '/settings') and contains(@class, 'menu-button-block w-inline-block')]")

# @when ('Click on Subscription & payments option.')
# def click_subscription_and_payments(context):
#     context.app.find_element(By.CSS_SELECTOR, 'menu-button-text').click()

# @when ('Verify the right page opens.')
# def verify_right_page_opens(context):
#     pass


# @when ('Click on off plan on the left side menu')
# def click_off_plan_at_left_side_menu(context):
#     context.app.find_element(By.CSS_SELECTOR, 'menu-text').click()
#     # when i click on off plan option it stays on the same page ????
#     #sadiqul viewed this step and witness that when clicking on the "off plan" option it does not change to another page.
# #
# @when ('Verify the right page opens')
# def verify_the_right_page_opens(context):
#     page = LoginPage(context.driver)
#     actual_title= page.get_page_title()
#     expected_title= "page-title"
#     assert actual_title= expected_title
#    # ??? did i enter everything correctly above?
#
#  @then ('Filter the products by price range from 1200000 to 2000000')
# def filter_products_by_price_range_from_1200000_to_2000000(context):
#
#  @then ('Verify the price in all cards is inside the range (1200000 - 2000000)')
# def verify_the_price_in_all_cards_is_inside_the_range_1200000_2000000(context):
#
#
#
