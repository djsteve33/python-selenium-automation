from selenium.webdriver.common.by import By
from behave import then, when

CART = (By.ID, 'nav_cart_count')

@when('Open cart page')
def open_cart_page(context):
    context.driver.get("https://www.amazon.com/gp/cart/view.html?ref_=sw_gtc")

@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-truncate-cut']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

# @then('Verify cart has {expected_count} item(s)')
# def verify_cart_count(context, expected_count):
#     actual_text = context.driver.find_element(*CART).text
#     assert expected_count == actual_text, f'Expected {expected_count} but got actual {actual_text}'

# @then('Verify that text {expected_result} is shown')
# def verify_search_result(context, expected_result):
#     actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-truncate-cut']").text
#     assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
