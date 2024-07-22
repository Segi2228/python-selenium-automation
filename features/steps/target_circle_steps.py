from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Open Target Circle page
@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')
    sleep(5)


@then('Verify page has {number}benefit cells')
def verify_benefit_cells(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[class*='h-margin-b-tiny']")
    assert len(cells) == number, f'{number} is not equal to {len(cells)}'
