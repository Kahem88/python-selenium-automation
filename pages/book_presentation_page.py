from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BookPresentationPage(Page):
    YOUR_COUNTRY = (By.ID, 'Your-country')
    COMPANY_NAME = (By.ID, 'Company-name-2')
    POSITION = (By.ID, 'Position')
    YOUR_NAME = (By.ID, 'Director-name')
    YOUR_PHONE = (By.ID, 'Director-phone')
    AMOUNT_OF_AGENTS_IN_COMPANY = (By.ID, 'Amount-of-agents-in-company')
    EMAIL = (By.ID, 'Email-2')
    country_text = 'United States'
    company_text = 'Careerist'
    position_text = 'QA Engineer'
    phone_text = '123456789'
    amount_of_agents_in_company_text = '2'
    name_text = 'Kahem'
    email_text = 'kahempatrick89@yahoo.com'

    BUTTON_1 = (By.CSS_SELECTOR, '[value="Send request"]')
    BUTTON_2 = (By.CSS_SELECTOR, '.step-button.margin-bottom-8.w-button')

    def input_fields(self):
        self.driver.find_element(*self.YOUR_COUNTRY).send_keys(self.country_text)
        self.driver.find_element(*self.COMPANY_NAME).send_keys(self.company_text)
        self.driver.find_element(*self.POSITION).send_keys(self.position_text)
        self.driver.find_element(*self.YOUR_PHONE).send_keys(self.phone_text)
        self.driver.find_element(*self.AMOUNT_OF_AGENTS_IN_COMPANY).send_keys(self.amount_of_agents_in_company_text)
        self.driver.find_element(*self.EMAIL).send_keys(self.email_text)
        self.driver.find_element(*self.YOUR_NAME).send_keys(self.name_text)
        sleep(5)

    def verify_information_is_present(self):
        expected_country_text = 'United States'
        field_1 = self.find_element(*self.YOUR_COUNTRY)
        actual_country_text = field_1.get_attribute("value")
        assert expected_country_text in actual_country_text, f'Expected({expected_country_text}) is not present in Actual({actual_country_text})'
        # expected_country_text = 'United States'
        # actual_country_text = self.find_element(*self.YOUR_COUNTRY).text
        # assert expected_country_text == actual_country_text, f'Expected({expected_country_text}) is not present in Actual({actual_country_text})'

        expected_company_name_text = 'Careerist'
        field_2 = self.find_element(*self.COMPANY_NAME)
        actual_company_name_text = field_2.get_attribute("value")
        assert expected_company_name_text in actual_company_name_text, f'Expected({expected_company_name_text}) is not present in Actual({actual_company_name_text})'

        expected_position_text = 'QA Engineer'
        field_3 = self.find_element(*self.POSITION)
        actual_position_text = field_3.get_attribute("value")
        assert expected_position_text in actual_position_text, f'Expected({expected_position_text}) is not present in Actual({actual_position_text})'

        expected_your_phone_text = '123456789'
        field_4 = self.find_element(*self.YOUR_PHONE)
        actual_your_phone_text = field_4.get_attribute("value")
        assert expected_your_phone_text in actual_your_phone_text, f'Expected({expected_your_phone_text}) is not present in Actual({actual_your_phone_text})'

        expected_amount_of_agents_in_company_text = '2'
        field_5 = self.find_element(*self.AMOUNT_OF_AGENTS_IN_COMPANY)
        actual_amount_of_agents_in_company_text = field_5.get_attribute("value")
        assert expected_amount_of_agents_in_company_text in actual_amount_of_agents_in_company_text, f'Expected({expected_amount_of_agents_in_company_text}) is not present in Actual({actual_amount_of_agents_in_company_text})'

        expected_email_text = 'kahempatrick89@yahoo.com'
        field_6 = self.find_element(*self.EMAIL)
        actual_email_text = field_6.get_attribute("value")
        assert expected_email_text in actual_email_text, f'Expected({expected_email_text}) is not present in Actual({actual_email_text})'

        expected_name_text = 'Kahem'
        field_7 = self.find_element(*self.YOUR_NAME)
        actual_name_text = field_7.get_attribute("value")
        assert expected_name_text in actual_name_text, f'Expected({expected_name_text}) is not present in Actual({actual_name_text})'

    def scroll_down(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END)
        actions.perform()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # def is_request_button_available(self):
    #     return self.driver.find_element(*self.BUTTON_1).is_displayed()

    # wait_for_button_clickable


    def wait_for_button_clickable_available(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_1)
        )
    def wait_for_subscription_clickable_available(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BUTTON_2)
        )
