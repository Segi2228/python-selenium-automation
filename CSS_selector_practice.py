from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Find by css, using id:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox") # driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")

# Find by css, using classes:
driver.find_element(By.CSS_SELECTOR, ".nav-input")
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute.nav-input")
# tag + classes
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute.nav-input")
# tag + id + classes
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-progressive-attribute.nav-input")
# attributes:
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']")
# tag + attributes
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][type='text']")
# tag + #id + .class + [attributes]
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon'][type='text']")
# Order doesn't matter (although it's recommended to have: tag + #id + .class + [attributes])
driver.find_element(By.CSS_SELECTOR, "input[type='text'].nav-input[placeholder='Search Amazon']#twotabsearchtextbox")

# Attributes, partial match
driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search Ama']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[class*='ap_signin_notification_privacy_notice']")

# Multiple nodes,  parent => child
driver.find_element(By.CSS_SELECTOR, "div.a-box div#legalTextRow a[href*='condition']")








#  25 changes: 25 additions & 0 deletions25
# features/steps/target_search_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,25 @@
# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# @given('Open target main page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')
#
#
# @when('Search for product')
# def search_product(context):
#     # find search field and enter text
#     context.driver.find_element(By.ID, 'search').send_keys('tea')
#     # click search
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     # wait for the page with search results to load
#     sleep(6)
#
#
# @then('Verify search worked')
# def verify_search_results(context):
#     expected_text = 'tea'
#     actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'
#  11 changes: 11 additions & 0 deletions11
# features/tests/target_search.feature
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,11 @@
# Feature: Target main page search tests
#
#   Scenario: User can search for a product on target
#     Given Open target main page
#     When Search for product
#     Then Verify search worked
#
#   # Make sure scenario names are unique:
#   Scenario: User can search for a product2 on target
#     Given Open target main page
#     # .....
#  29 changes: 29 additions & 0 deletions29
# target_main_page_steps.py
# Original file line number	Diff line number	Diff line change
# @@ -0,0 +1,29 @@
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # Start Chrome browser:
# driver_path = ChromeDriverManager().install()
# driver = webdriver.Chrome(service=Service(driver_path))
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# # Open target.com
# driver.get('https://www.target.com/')
#
# driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
# driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
#
# expected = 'Sign into your Target account'
# actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'StyledHeading')]").text
# assert expected == actual, f'Expected {expected} did not match actual {actual}'
#
# # OR:
# # driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
#
# # Make sure login button is shown
# driver.find_element(By.ID, 'login')
