from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test = 'resultsHeading']")

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TEXT)
        # actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TEXT).text
        # assert expected_product in actual_text, f'Expected coffee but got {actual_text}'
        sleep(5)

    def verify_url(self, expected_product):
        expected_product = 'coffee'
        self.verify_partial_url(expected_product)
        # url = self.driver.current_url
        # assert expected_product in url, f'Expected "coffee" in url  but coffee is not in {url}'
