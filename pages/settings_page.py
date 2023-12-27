from selenium.webdriver.common.by import By
from pages.base_page import Page

class SettingsPage(Page):

    subscription_and_payments = (By.XPATH, "//a[contains(@href, '/subscription') and contains(@class, 'page-setting-block w-inline-block')]")
    actual_url = 'https://soft.reelly.io/subscription'
    def click_subscription_and_payments(self):
        self.click(*self.subscription_and_payments)

    # def is_page_displayed(self):
    #     return self.driver.find_element(*self.'SUBSCRIPTION_AND_PAYMENTS').is_displayed()

    def verify_right_page_opens(self):
        expected_url = 'https://soft.reelly.io/subscription'
        actual_url = 'https://soft.reelly.io/subscription'
        assert actual_url == expected_url, f'Expected {expected_url} but got {actual_url}'

# context.driver.actual_url