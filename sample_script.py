# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# #driver_path = ChromeDriverManager().install()
# driver_path = r'C:\Users\lozak\python-selenium-automation\chromedriver.exe'
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()

# # open the url
# driver.get('https://www.google.com/')
#
# # populate search field
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Table')
#
# # wait for 4 sec
# sleep(4)
#
# # click search button
# driver.find_element(By.NAME, 'btnK').click()
#
# # verify search results
# assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')
#
# driver.quit()

#
#driver.get('https://www.target.com/')


#
# #search for tea
# actual_text = driver.find_element(By.CSS_SELECTOR,"[data-test = '@web/Search/SearchInput']").send_keys('tea')
# expected_text = 'tea'
#
#
# # # #click on search icon
# driver.find_element(By.CSS_SELECTOR,"[data-test = '@web/Search/SearchButton']").click()
#
# assert expected_text in actual_text,f'{expected_text} not found in {actual_text}'
# search for product
# driver.find_element(By.XPATH, "//input[@data-test= '@web/Search/SearchInput']").send_keys('tea')
# # click on search
# driver.find_element(By.XPATH, "//button[@data-test= '@web/Search/SearchButton']").click()
#
# expected_text = 'tea'
# actual_text = driver.find_element(By.XPATH,"//div[@data-test = 'resultsHeading']").text
#
# assert expected_text in actual_text
# print('Test passed')
# sleep(5)
#, f'{expected_text}is not in {actual_text}'
#
# # Click on search and search for item
# driver.find_element(By.CSS_SELECTOR,"[data-test = '@web/Search/SearchInput']").send_keys('teatree oil')
# # expected_text = 'tea'
# #
#
 # click on search icon
# driver.find_element(By.CSS_SELECTOR,"[data-test = '@web/Search/SearchButton']").click()
# sleep(10)
# ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] button[id*='addToCartButton']")
# VIEW_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] a[href='/cart']")
#
#
# driver.find_element(*ADD_TO_CART_BUTTON ).click()
# sleep(10)
#
# driver.find_element(*ADD_TO_CART).click()
# sleep(10)
#
# driver.find_element(*VIEW_CART).click()
# sleep(10)
# ACTUAL_ITEM = driver.find_element(By.CSS_SELECTOR,"[data-test='cart-summary-item-count']")
# sleep(5)
# EXPECTED_ITEM = ACTUAL_ITEM.text
# assert EXPECTED_ITEM in ACTUAL_ITEM.text, f'{EXPECTED_ITEM} is not in {ACTUAL_ITEM.text}'
# print('test passed')