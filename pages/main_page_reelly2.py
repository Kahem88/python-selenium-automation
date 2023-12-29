import time

from selenium.webdriver.common.by import By
from pages.base_page import Page
import time
from selenium.webdriver.support import expected_conditions as EC

# locator_1 = (By.ID, "email-2")
# locator_2 = (By.ID, "field")
#
# menu_button = (By.ID, "menu-button-text")
# connect_the_company_button = (By.CSS_SELECTOR, ".get-free-period.menu")
# login_btn = (By.CSS_SELECTOR, 'a.login-button[wized="loginbutton"]')




class MainPage2(Page):

    EMAIL = (By.CSS_SELECTOR, 'input#email-2[type="email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input#field[type="password"]')
    LOGIN = (By.CSS_SELECTOR, 'a.login-button[wized="loginButton"]')
    COMPANY_BTN = (By.XPATH, "//div[text()='Connect the company']")

    def open_reelly_page(self):
        self.driver.get('https://soft.reelly.io/')


    def log_in(self):


        # self.input_text('Kahempatrick88@yahoo.com', *self.locator_1)
        # self.input_text('Juanita$88', *self.locator_2)
        # self.click(*self.login_btn)
        # sleep(5)
        time.sleep(10)
        self.input("Kahempatrick88@yahoo.com", *self.EMAIL)
        self.input("Juanita$88", *self.PASSWORD)
        self.click(*self.LOGIN)

        time.sleep(2)



    def click_connect_page(self):
        self.wait_for_visible(self.COMPANY_BTN).click()
        time.sleep(2)

    # def click(self, *locator):
    #     self.driver.find_element(connect_the_company_button).click()








