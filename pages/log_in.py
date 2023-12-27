from pages.base_page import Page
from selenium.webdriver.common.by import By


class login(Page):
    # ACTUAL_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    CONTINUE_BTN = (By.CSS_SELECTOR, ".login-button")

    def sign_in(self):
        self.find_element(*self.EMAIL_FIELD).send_keys("kahempatrick88@yahoo.com")
        self.find_element(*self.PASSWORD_FIELD).send_keys("Juanita$88")
        # self.input_text("Juanita$88", *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BTN)
