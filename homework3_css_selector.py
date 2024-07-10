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

# find by css, using classes:
# Amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-link-nav-icon")

# Create account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Name field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# mobile number or email
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# password field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# password must be 6 char ...
#
driver.find_element(By.CSS_SELECTOR, "div[class*='auth-inlined-information-message'] div.a-alert-content")


# re_enter password
#by id
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
# by id and attribute
driver.find_element(By.CSS_SELECTOR, "#ap_password_check[name = 'passwordCheck']")

# Create account
# by id + class
driver.find_element(By.CSS_SELECTOR, "#continue.a-button-input")
# by Id + attribute
driver.find_element(By.CSS_SELECTOR, "#continue[type='submit']")

# you agree to Amazon's...
# Attributes, partial match
# condition of use
driver.find_element(By.CSS_SELECTOR,"a[href*='ap_register_notification_condition_of_use']")
# privacy
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

# Sign in
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")