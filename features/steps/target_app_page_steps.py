from selenium.webdriver.common.by import By
from behave import given, then, when
from time import sleep

@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()

@given('Store original window')
def store_original_window(context):
    # why calling from target_app _page not working?
    context.original_window = context.app.base_page.get_current_window()
    # context.original_window = context.driver.current_window_handle
    #print('original window', context.original_window)

@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()

@when('Switch to new window')
def switch_window(context):
   context.app.base_page.switch_to_new_window()

@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.privacy_policy_page.verify_pp_url()


@then('Close current page')
# QUESTION:
# how does it know to close current window? we don't pass any url
def close(context):
    context.app.base_page.close()

@then('Return to original window')
def return_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)


# TERMS AND CONDITIONS STEPS
@then('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window()

@then('Click on Target terms and conditions link')
def click_tc_link(context):
 context.app.target_app_page.click_cc_link()

@then('Switch to new opened window')
def switch__new_window(context):
 context.app.target_app_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
  context.app.terms_and_conditions_page.verify_tc_url()



