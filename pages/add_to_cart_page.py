from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class AddToCartPage(Page):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] button[id*='addToCartButton']")
    VIEW_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] a[href='/cart']")
    SIDE_NSV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


    def search_item(self):
        pass
     # wanted to reuse the search product under main_page_steps
    def click_cart(self):
       self.wait_and_click(*self.ADD_TO_CART_BUTTON)


    def store_product_name(self, name):
       self.wait_for_element_appear(*self.SIDE_NSV_PRODUCT_NAME)


    def add_to_cart(self):
      self.wait_and_click(*self.ADD_TO_CART)


    def view_cart(self):
        self.wait_and_click(*self.VIEW_CART)

