from pages.base_page import Page


class MainPage(Page):

    def open_main_url(self):
        self.open_url('https://www.amazon.com/')

    def open_product(context, product_id):
        context.driver.get(
            f'https://www.amazon.com/Wrangler-Authentics-Classic-Relaxed-Stretch/dp/{product_id}/')