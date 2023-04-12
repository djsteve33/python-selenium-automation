from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    EMPTY_CART_TITLE = (By.XPATH, "//h2[contains(text(), 'Your Amazon Cart')]")

    def verify_cart_is_empty(self):
        expected_text = "Your Amazon Cart is empty"
        self.verify_text(expected_text, *self.EMPTY_CART_TITLE)
        # actual_res = self.find_element(*self.EMPTY_CART_TITLE).text
        # assert expected_res == actual_res, f'Expected {expected_res} but got actual {actual_res}'
