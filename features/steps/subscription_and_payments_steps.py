from behave import given, when, then
from selenium.webdriver.common.by import By


@then('Verify title “Subscription & payments” is visible.')
def verify_title_subscription_and_payments_is_visible(context):
    context.app.subscription_and_payments_page.verify_title_subscription_and_payments_is_visible()


@then('Verify “back” and “upgrade plan” buttons are available.')
def verify_back_and_upgrade_plan_are_available(context):
    pass
