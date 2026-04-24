from pages.base_page import BasePage
from pages.locators import locators_cart_page as lcp


class CustomerCartPage(BasePage):
    page_url = '/shop/cart'

    def check_page_title_is(self, text):
        title = self.find(lcp.title_loc)
        assert title.text == text

    def check_page_info_is(self, text):
        text_info = self.find(lcp.text_info_loc)
        assert text_info.text == text

    def check_page_button_sing_in(self, text_log, text_pass):
        button_sing_in = self.find(lcp.button_sign_in)
        button_sing_in.click()
        text_login = self.find(lcp.text_email)
        text_password = self.find(lcp.text_pass)
        assert text_login.text == text_log
        assert text_password.text == text_pass

    def check_page_cart_contact_us(self, text):
        link_phone_number = self.find(lcp.contact_us_loc)
        link_phone_number.click()
        contact_us_title_page = self.find(lcp.contact_us_loc)
        assert contact_us_title_page.text == text
