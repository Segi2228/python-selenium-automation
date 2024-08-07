from multiprocessing import context
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] button[id*='addToCartButton']")
# VIEW_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] a[href='/cart']")
# SIDE_NSV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
# ACTUAL_ITEM_IN_CART = (By.CSS_SELECTOR, "[data-test='cartItem']")


@when('Search for teatree oil')
def search_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test = '@web/Search/SearchInput']").send_keys('teatree oil')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test = '@web/Search/SearchButton']").click()
    sleep(10)


@then('Click on Add to Cart button')
def click_cart(context):
    context.app.add_to_cart_page.click_cart()
    # the above slip is replaced by this but throws an error
    # context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON))
    #context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    # sleep(10)

# another way to verify the product in side nav is the one in cart, we can store the prod name
@then('store product name')
def store_product_name(context):
    context.app.add_to_cart_page.store_product_name
    # context.driver.wait.until(EC.visibility_of_element_located(SIDE_NSV_PRODUCT_NAME))
    # context.product_name = context.driver.find_element(*SIDE_NSV_PRODUCT_NAME).text


@then('Add item to cart')
def add_to_cart(context):
    context.app.add_to_cart_page.add_to_cart()
    # CHECK IF THIS MAKES SENSE
    #context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()
    #context.driver.find_element(*ADD_TO_CART).click()
    # sleep(6)

@then('View cart')
def view_cart(context):
    context.app.add_to_cart_page.view_cart()
    # context.driver.wait.until(EC.element_to_be_clickable(VIEW_CART)).click()
    #HOW CAN I REPLACE THE NEXT SLEEP?
    # sleep(10)

# rather than clicking add cart and checkout option on side nav, we can directly connect to the cart page
# @then('Open Cart page')
# def view_cart(context):
#     context.driver.get('https://www.target.com/cart')
#     sleep(6)


# @then('Verify cart has the item')
# def verify_cart(context):
#     ACTUAL_ITEM = context.driver.find_element(*ACTUAL_ITEM_IN_CART).text
#     #EXPECTED_ITEM = context.driver.find_element(*SIDE_NSV_PRODUCT_NAME).text
#     expected_text = 'tea tree'
#     assert expected_text in ACTUAL_ITEM.lower(), f'{expected_text} is not in {ACTUAL_ITEM}'

@then('Verify cart has the item')
def verify_cart(context):
    # ACTUAL_ITEM = context.driver.find_element(*ACTUAL_ITEM_IN_CART).text
    # assert context.product_name in ACTUAL_ITEM, f'{context.product_name} does not match{ACTUAL_ITEM}'
    context.app.cart_page.verify_cart()
