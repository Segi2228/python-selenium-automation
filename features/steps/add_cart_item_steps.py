from multiprocessing import context
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] button[id*='addToCartButton']")
VIEW_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] a[href='/cart']")
SIDE_NSV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
ACTUAL_ITEM_IN_CART = (By.CSS_SELECTOR, "[data-test='cartItem']")


@when('Search for teatree oil')
def search_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test = '@web/Search/SearchInput']").send_keys('teatree oil')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test = '@web/Search/SearchButton']").click()
    sleep(10)


@then('Click on Add to Cart button')
def click_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    sleep(10)


@then('Add item to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(6)
    context.driver.find_element(*VIEW_CART).click()
    sleep(10)


@then('Open Cart page')
def view_cart(context):
    context.driver.get('https://www.target.com/cart')
    sleep(6)


@then('Verify cart has the item')
def verify_cart(context):
    ACTUAL_ITEM = context.driver.find_element(*ACTUAL_ITEM_IN_CART).text
    #EXPECTED_ITEM = context.driver.find_element(*SIDE_NSV_PRODUCT_NAME).text
    expected_text = 'tea tree'
    assert expected_text in ACTUAL_ITEM.lower(), f'{expected_text} is not in {ACTUAL_ITEM}'
