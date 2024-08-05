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
# driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
# sleep(5)
# # driver.find_element(By.XPATH,"//li[@id='listaccountNav-signIn']").click()
# driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
# sleep(5)
# # verify
# expected_text = 'Sign into your Target account'
# #expected_text = 'Sign in'
#
# actual_text = driver.find_element(By.XPATH,"//div[@id='__next']").text
# assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text{actual_text}'
# # #print(actual_text)
# #
# driver.find_element(By.XPATH, "//button[@id='login']")
# print('Test passed')
