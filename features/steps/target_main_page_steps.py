from multiprocessing import context

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# open target main page
@given('Open Target main page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')


# Search for product

@when('Search for product')
def search_products(context):
    # find search box and enter text
    context.driver.find_element(By.XPATH, "//input[@data-test= '@web/Search/SearchInput']").send_keys('tea')
    # click on search button
    context.driver.find_element(By.XPATH, "//button[@data-test= '@web/Search/SearchButton']").click()

    sleep(5)



# Click on sign in icon
@when('Click on Sign In icon')
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()


# click on sign in again
@when('Click on Sign In icon again')
def click_signin_again(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(5)




# Click on cart icon
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()
    sleep(5)



