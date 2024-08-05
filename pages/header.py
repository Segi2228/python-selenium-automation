from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.XPATH, "//input[@data-test= '@web/Search/SearchInput']")
    SEARCH_BTN = (By.XPATH, "//button[@data-test= '@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon']")

    def search(self, product):
        # print('POM layer: ', product)
        self.input_text(product,*self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)
