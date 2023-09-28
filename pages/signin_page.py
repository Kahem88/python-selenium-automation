from pages.base_page import Page
from selenium.webdriver.common.by import By


class SigninPage(Page):

    ACTUAL_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'ap_email')

    def verify_signin_page_opened(self, expected_text):
        # expected_text = 'Sign in'
        actual_text = self.find_element(*self.ACTUAL_TEXT).text
        assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'
        self.find_element(*self.EMAIL_FIELD)

