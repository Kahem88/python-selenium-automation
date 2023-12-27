from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

locator_1 = (By.ID, "email-2")
locator_2 = (By.ID, "field")
menu_button = (By.ID, "menu-button-text")


class MainPage(Page):

    def open_reelly_signup_page(self):
        self.driver.get('https://soft.reelly.io/')
        sleep(5)

    def log_in(self):
        self.input_text('Kahempatrick88@yahoo.com', *locator_1)
        self.input_text('Juanita$88', *locator_2)

    def click(self, *locator):
        self.driver.find_element(*locator).click()
