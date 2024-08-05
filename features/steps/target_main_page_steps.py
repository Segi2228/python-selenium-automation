from itertools import product
from multiprocessing import context
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
# LOGIN_BTN = (By.CSS_SELECTOR, "[id='login']")
# CART_BTN = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon']")


# open target main page
@given('Open Target main page')
def open_target_page(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open()


# Search for product

@when('Search for {product}')
def search_products(context, product):
    context.app.header.search(product)

    # # find search box and enter text
    # context.driver.find_element(By.XPATH, "//input[@data-test= '@web/Search/SearchInput']").send_keys('tea')
    # # click on search button
    # context.driver.find_element(By.XPATH, "//button[@data-test= '@web/Search/SearchButton']").click()
    #
    # sleep(5)



# Click on sign in icon
@when('Click on Sign In icon')
def click_signin(context):
    # context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
    context.app.header.click_signin()


# click on sign in again
@when('Click on Sign In icon again')
def click_signin_again(context):
    context.app.header.click_signin_again()
    # context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN)).click()
    # sleep(5)
    # sign_in_page_open= context.driver.find_element(By.CSS_SELECTOR, "[id='login']")
    # context.driver.wait.until(EC.element_to_be_clickable(LOGIN_BTN))
    # or I can use
    # context.driver.wait.until(EC.new_window_is_opened())


# Click on cart icon
@when('Click on Cart icon')
def click_cart(context):
     context.app.header.click_cart()
     #   context.driver.wait.until(EC.element_to_be_clickable(CART_BTN)).click()
     #   # actual_text_shown = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
     #   context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")))
     # # sleep(5)
