from multiprocessing import context
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify search shows for {expected_product}')
def verify_search_result(context, expected_product):
    # expected_text = 'tea'
    # actual_text = context.driver.find_element(By.XPATH, "//div[@data-test = 'resultsHeading']").text
    # assert expected_text in actual_text, f'Expected {expected_text} but got {actual_text}'
    # sleep(5)

    context.app.search_results_page.verify_search_results(expected_product)


@then('Verify correct search results URL opens for {expected_product}')
def verify_search_url(context, expected_product):
    context.app.search_results_page.verify_url(expected_product)
