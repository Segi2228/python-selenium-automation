from pages.base_page import Page


class MainPage(Page):

    def open(self):
        self.driver.get('https://www.target.com/')
