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

# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo' and @aria-label='Amazon']")

# Email field
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.XPATH, "//input[@aria-describedby='Enter your email or mobile phone number']")
driver.find_element(By.XPATH, "//*[@aria-describedby='Enter your email or mobile phone number']")
# Continue button
driver.find_element(By.ID, 'continue')

# Conditions of use link
####### NEED HELP ON how to navigate specifically to the conditions of use excluding privacy link
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[contains(text(),'Conditions of Use')]")
# Privacy Notice link

driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Privacy Notice')]")
# Need help link
####### NEED HELP ON the best practice how to choose  locators. is it before/after the help link expanded/collapsed
driver.find_element(By.XPATH, "//div[@class='a-row a-expander-container a-expander-inline-container']")


# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")


# Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link')
driver.find_element(By.XPATH,"//a[@id='ap-other-signin-issues-link' and @class='a-link-normal']")

# Create your Amazon account button
driver.find_element(By.ID, 'auth-create-account-link')
