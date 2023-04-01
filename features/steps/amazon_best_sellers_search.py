from selenium.webdriver.common.by import By
from behave import given, then, when

BEST_SELLERS = (By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
BEST_SELLER_LINKS = (By.XPATH, "//a[contains(@href,'ref=zg_bs_tab')]")

# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')

@when('Click on Best Sellers link')
def click_best_sellers(context):
    context.driver.find_element(*BEST_SELLERS).click()

@then('Verify there are {expected_amount} links')
def verify_best_sellers_link_count(context, expected_amount):
    expected_amount = int(expected_amount)

    best_seller_links = context.driver.find_elements(*BEST_SELLER_LINKS)
    assert len(best_seller_links) == expected_amount, f'Expected {expected_amount} links, but got {len(best_seller_links)}'

