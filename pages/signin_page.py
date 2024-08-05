from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
  LOGIN_BTN = (By.CSS_SELECTOR, "[id='login']")
  ACTUAL_TEXT = (By.CSS_SELECTOR, "#login")



  def sign_in_form(self):
        expected_text = 'Sign in with password'
        self.wait_until_clickable(*self.LOGIN_BTN)
        self.verify_partial_text(expected_text, *self.ACTUAL_TEXT)


