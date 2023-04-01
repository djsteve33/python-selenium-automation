from selenium.webdriver.common.by import By
from behave import given, when, then

AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click on Orders')
def click_orders(context):
    context.driver.find_element(By.ID, "nav-orders").click()

@then('Verify {expected_result} header is visible')
def verify_sign_in_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in')]").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

@then('Verify email input field is present')
def verify_email_input_field_result(context, ):
    actual_result_2 = context.driver.find_element(By.XPATH, "//input[@type='email']")
    # assert expected_result_2 == actual_result_2, f'Expected {expected_result_2} but got actual {actual_result_2}'


@given('Click on Amazon icon')
def click_icon(context):
    context.driver.find_element(By.XPATH, "//*[@aria-label='Amazon']").click()

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count').click()

@then('Verify cart is empty')
def verify_cart_results(context):
    expected_res = "Your Amazon Cart is empty"
    actual_res = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Your Amazon Cart')]").text
    assert expected_res == actual_res, f'Expected {expected_res} but got actual {actual_res}'

@when('Input text {text}')
def input_search_word(context, text):
    context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)

@when('Click on search button')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()