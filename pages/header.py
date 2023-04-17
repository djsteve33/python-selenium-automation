from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    ORDERS = (By.ID, "nav-orders")
    # CART_ICON = (By.CSS_SELECTOR, '#nav-cart-count')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    CLOTHING_OPTIONS = (By.XPATH, "//a[starts-with(@href, '/New-Arrivals/b/?')]")
    WOMEN_OPTION = (By.XPATH, "//a[contains(@href, 'womens&bbn')]")

    def input_search_text(self, text):
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_orders(self):
        self.click(*self.ORDERS)

    def click_on_cart_icon(self):
        self.click(*self.CART_ICON)

    def select_department(self, alias):
        department_dd = self.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(department_dd)
        select.select_by_value(f'search-alias={alias}')

    def hover_clothing_options(self):
        clothing_options = self.find_element(*self.CLOTHING_OPTIONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(clothing_options)
        actions.perform()

    def verify_women_option_shown(self):
        self.wait_for_element_appear(*self.WOMEN_OPTION)