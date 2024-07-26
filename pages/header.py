from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.XPATH, "//input[@data-test= '@web/Search/SearchInput']")
    SEARCH_BTN = (By.XPATH, "//button[@data-test= '@web/Search/SearchButton']")

    def search(self):
        self.input_text('coffee',*self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)