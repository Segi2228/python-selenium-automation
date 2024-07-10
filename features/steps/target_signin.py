from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# open target main page
# @given('Open Target page')
# def open_target_page(context):
#  context.driver.get('https://www.target.com/')

 # Click on sign in icon
@when('Click on Sign In icon')
def click_signin(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()

# click on sign in again
@when('Click on Sign In icon again')
def click_signin_again(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(5)


#Verify sign in form opens

@then('Sign in form opens')
def sign_in_form(context):
    actual = context.driver.find_element(By.CSS_SELECTOR, "#login").text
    expected = 'Sign in with password'
    assert expected in actual, f'Expected text {expected} is not in actual text{actual}'
    print('Test passed')

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# # open the url
# driver.get('https://www.target.com/')
# # find sign-in and click
# driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
#
# # Click Sign in again
# driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
# sleep(5)
#
#
# # # verify
#
# actual = driver.find_element(By.CSS_SELECTOR, "#login").text
# expected = 'Sign in with password'
#
# assert expected in actual, f'Expected text {expected} is not in actual text{actual}'

# print('Test passed')