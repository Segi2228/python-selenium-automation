from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class PrivacyPolicyPage(Page):
    def verify_pp_url(self):
        self.verify_partial_url('/target-privacy-policy')
