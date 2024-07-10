from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# open target page
@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


# Click on cart icon
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()
    sleep(5)


# Verify empty cart message
@then('Your cart is empty message shown')
def verify_empty_cart(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text{actual_text}'
    print('Test passed')





