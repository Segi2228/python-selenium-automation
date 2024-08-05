from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    ACTUAL_ITEM_IN_CART = (By.CSS_SELECTOR, "[data-test='cartItem']")


    def verify_empty_cart(self):
        expected_text = 'Your cart is empty'
        #message_ = self.find_element(*self.CART_EMPTY_MSG).text
        #print(message_)
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text(expected_text, *self.CART_EMPTY_MSG)
        # actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        # assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text{actual_text}'


    def verify_cart(self):
        expected_text = 'teatree'
        self.verify_partial_text(expected_text, *self.ACTUAL_ITEM_IN_CART)
