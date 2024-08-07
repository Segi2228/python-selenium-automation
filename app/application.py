from pages.add_to_cart_page import AddToCartPage
from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.signin_page import SignInPage
from pages.add_to_cart_page import AddToCartPage
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.terms_and_conditions_page import TermsAndConditions

class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)

        self.target_app_page = TargetAppPage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.signin_page = SignInPage(driver)
        self.add_to_cart_page = AddToCartPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.terms_and_conditions_page = TermsAndConditions(driver)

