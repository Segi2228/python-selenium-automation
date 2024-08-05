from multiprocessing import context

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Verify empty cart message
@then('Your cart is empty message shown')
def verify_empty_cart(context):
    sleep(5)
    context.app.cart_page.verify_empty_cart()

    # expected_text = 'Your cart is empty'
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']h1").text
    # assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text{actual_text}'
