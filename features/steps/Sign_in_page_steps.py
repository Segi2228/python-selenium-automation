from multiprocessing import context

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Verify sign in form opens

@then('Sign in form opens')
def sign_in_form(context):
    context.app.signin_page.sign_in_form()
    # actual = context.driver.find_element(By.CSS_SELECTOR, "#login").text
    # expected = 'Sign in with password'
    # assert expected in actual, f'Expected text {expected} is not in actual text{actual}'
    # print('Test passed')
