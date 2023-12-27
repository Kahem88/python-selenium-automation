from pages.base_page import Page
from pages.main_page_reelly2 import MainPage2
from pages.book_presentation_page import BookPresentationPage
# from pages.login_page import LoginPage
# from pages.off_plan_page import OffPlanPage
# from pages.product_details_page import ProductDetailsPage
# from pages.verify_reelly_connect_company import ReellyConnectCompanyPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page_reelly2 = MainPage2(driver)
        self.book_presentation_page = BookPresentationPage(driver)
        # self.login_page = LoginPage(driver)
        # self.off_plan_page = OffPlanPage(driver)
        # self.product_details_page = ProductDetailsPage(driver)
        # self.verify_reelly_connect_company = ReellyConnectCompanyPage(driver)



# from pages.base_page import Page
# from pages.main_page_reelly2 import MainPage2
#
#
# class Application:
#     def __int__(self, driver):
#         self.page = Page(driver)
#         self.main_page_reelly2 = MainPage2(driver)
#


# from pages.main_page_reelly import MainPage
# from pages.log_in import login
# from pages.settings_page import SettingsPage
# from pages.header import Header
# from pages.search_result_page import SearchResultPage
# from pages.signin_page import SigninPage
# from pages.main_page_reelly import MainPage
# from pages.subscription_and_payments_page import SubscriptionAndPayments
#
#
# class Application:
#
#     def __init__(self, driver):
#         self.main_page_reelly = MainPage(driver)
#         self.log_in = login(driver)
#         self.settings_page = SettingsPage(driver)
#         # self.base_page = Page(driver)
#         self.subscription_and_payments_page = SubscriptionAndPayments(driver)
#         # self.header = Header(driver)
#         # self.signin_page = SigninPage(driver)
#         # self.reelly_class = MainPage(driver)

