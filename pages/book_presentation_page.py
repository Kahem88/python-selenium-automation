from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BookPresentationPage(Page):
    YOUR_COUNTRY = (By.ID, 'Your-country')
    COMPANY_NAME = (By.ID, 'Company-name-2')
    POSITION = (By.ID, 'Position')
    YOUR_NAME = (By.ID, 'Director-name')
    YOUR_PHONE = (By.ID, 'Director-phone')
    AMOUNT_OF_AGENTS_IN_COMPANY = (By.ID, 'Amount-of-agents-in-company')
    EMAIL = (By.ID, 'Email-2')
    text = 'United States'
    company_text = 'Careerist'
    position_text = 'QA Engineer'
    phone_text = '123456789'
    amount_of_agents_in_company_text = '2'
    name_text = 'Kahem'
    email_text = 'kahempatrick89@yahoo.com'

    BUTTON_1 = (By.CSS_SELECTOR, 'purchase-access.w-button')

    def input_fields(self):
        self.driver.find_element(*self.YOUR_COUNTRY).send_keys(self.text)
        self.driver.find_element(*self.COMPANY_NAME).send_keys(self.company_text)
        self.driver.find_element(*self.POSITION).send_keys(self.position_text)
        self.driver.find_element(*self.YOUR_PHONE).send_keys(self.phone_text)
        self.driver.find_element(*self.AMOUNT_OF_AGENTS_IN_COMPANY).send_keys(self.amount_of_agents_in_company_text)
        self.driver.find_element(*self.EMAIL).send_keys(self.email_text)
        self.driver.find_element(*self.YOUR_NAME).send_keys(self.name_text)
        sleep(5)

    def verify_information_is_present(self):
        expected_text = 'United States'
        actual_text = 'United States'
        assert expected_text == actual_text, f'Expected({expected_text}) is not present in Actual({actual_text})'

        expected_text = 'Careerist'
        actual_text = 'Careerist'
        assert expected_text == actual_text, f'Expected({expected_text}) is not present in Actual({actual_text})'

        expected_text = 'QA Engineer'
        actual_text = 'QA Engineer'
        assert expected_text == actual_text, f'Expected({expected_text}) is not present in Actual({actual_text})'

        expected_text = '123456789'
        actual_text = '123456789'
        assert expected_text == actual_text, f'Expected({expected_text}) is not present in Actual({actual_text})'

        expected_text = '2'
        actual_text = '2'
        assert expected_text == actual_text, f'Expected({expected_text}) is not present in Actual({actual_text})'

        expected_text = 'kahempatrick89@yahoo.com'
        actual_text = 'kahempatrick89@yahoo.com'
        assert expected_text == actual_text, f'Expected({expected_text}) is not present in Actual({actual_text})'

        expected_text = 'Kahem'
        actual_text = 'Kahem'
        assert expected_text == actual_text, f'Expected({expected_text}) is not present in Actual({actual_text})'

    def scroll_down(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END)
        actions.perform()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_request_button_available(self):
        return self.driver.find_element(*self.BUTTON_1).is_displayed()
