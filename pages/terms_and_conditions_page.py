from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class TermsAndConditions(Page):
    def verify_tc_url(self):
        self.verify_partial_url('/terms-conditions')
