from selenium.webdriver.common.by import By
from behave import then, when, given
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")

@given('Open Amazon T&C page')
def open_t_and_c_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle

@then('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()

@when('Switch to newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles
    context.driver.switch_to.window(windows[1])

@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_page_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))

@when('User can close new window and switch back to original')
def close_new_window_and_switch_to_original_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)







