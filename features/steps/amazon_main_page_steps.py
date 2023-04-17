from selenium.webdriver.common.by import By
from behave import given, when, then

# AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_ICON = (By.ID, 'nav-search-submit-button')

@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_url()
@when('Click on Orders')
def click_orders(context):
    context.app.header.click_orders()
    #context.driver.find_element(By.ID, "nav-orders").click()

@then('Verify {expected_result} header is visible')
def verify_sign_in_result(context, expected_result):
    context.app.sign_in_page.verify_sign_in_header(expected_result)
    #actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Sign in')]").text
    #assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

@then('Verify email input field is present')
def verify_email_input_field_result(context):
    context.app.sign_in_page.verify_email_field()
    #actual_result_2 = context.driver.find_element(By.XPATH, "//input[@type='email']")
    # assert expected_result_2 == actual_result_2, f'Expected {expected_result_2} but got actual {actual_result_2}'


@given('Click on Amazon icon')
def click_icon(context):
    context.driver.find_element(By.XPATH, "//*[@aria-label='Amazon']").click()

@when('Click on cart icon')
def click_cart_icon(context):
    # context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count').click()
    context.app.header.click_on_cart_icon()

@then('Verify cart is empty')
def verify_cart_results(context):
    # expected_res = "Your Amazon Cart is empty"
    # actual_res = context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Your Amazon Cart')]").text
    # assert expected_res == actual_res, f'Expected {expected_res} but got actual {actual_res}'
    context.app.cart_page.verify_cart_is_empty()

@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)


@when('Input text {text}')
def input_search_word(context, text):
    # context.driver.find_element(*AMAZON_SEARCH_FIELD).send_keys(text)
    context.app.header.input_search_text(text)

@when('Click on search button')
def click_search(context):
    # context.driver.find_element(*SEARCH_ICON).click()
    context.app.header.click_search()

@when('Hover over New Arrival options')
def hover_new_arrival_options(context):
    context.app.header.hover_clothing_options()

@then('Verify Women option present')
def verify_women_option(context):
    context.app.header.verify_women_option_shown()