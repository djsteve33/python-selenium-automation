from selenium.webdriver.common.by import By
from behave import then, when, given
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
#COLOR_TEXT = (By.CSS_SELECTOR, '#inline-twister-expanded-dimension-text-color_name')
COLOR_TEXT = (By.XPATH, "//div[@id='variation_color_name']/div/span")
#COLOR_OPTIONS = (By.XPATH, "//div[@id='inline-twister-expander-content-color_name']/div/div/ul/li/span/span")
COLOR_OPTIONS = (By.XPATH, "//button[@class='a-button-text']")
@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()

@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.app.main_page.open_product(product_id)

@then('Verify user can click through colors')
def verify_user_can_select_colors(context):
    all_color_options = context.driver.find_elements(*COLOR_OPTIONS)
    expected_colors = ["(Black)", '(Black/white)', '(Burgundy)', '(Burgundy/White)', '(Carolina Blue)',
                       '(Gray)', '(Hunter Green)', '(Hunter Green/White)', '(Hunter Green/Khaki)', '(Royal Blue)', '(Khaki)',
                       '(Lime Green)', '(Navy Blue)','(Navy Blue/White)', '(NavyBlue/Khaki)', '(Orange)',
                       '(Orange/White)', '(Purple)', '(Purple/White)', '(Red)', '(Gray)', '(Red/White)',
                       '(Red/White/Navy)', '(Royal Blue)', '(Royal Blue/White)', '(Teal Blue)', '(White)',
                       '(Yellow)', 'Black/Gold', 'Brown', '(Red/Black)', 'Gray', 'Navy Blue', 'Navy/Gold', 'Rainbow']
    print('Total colors:', len(all_color_options))
    for option in all_color_options:
        option.click()
        context.driver.wait.until(EC.element_to_be_clickable(COLOR_TEXT))
        color = context.driver.find_element(*COLOR_TEXT).text
        assert color in expected_colors, f"Expected color not found but found {color}"


