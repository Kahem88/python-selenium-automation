from pages.base_page import Page
from selenium.webdriver.common.by import By

class SubscriptionAndPayments(Page):
    HOME_PAGE_TITLE = (By.CSS_SELECTOR, '.lotion-your-h3--price.size')

  # BUTTON_1 = (By.ID, '.button-verify.w-inline-block')
  # BUTTON_2 = (By.ID, '.button-verify.margin-top-8.white.w-inline-block')

    def __init__(self, driver):
        self.driver = driver

    def verify_title_subscription_and_payments_is_visible(self):
        actual_title = self.find_element(*self.HOME_PAGE_TITLE).text
        expected_title = 'Subscription & payments'
        assert actual_title in expected_title, f"Expected title: '{expected_title}', Actual title: '{actual_title}'"

    def is_button_available(self, button_locator):
        return self.driver.find_element(*self.BUTTON_1).is_displayed()
        return self.driver.find_element(*self.BUTTON_2).is_displayed()