import time
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import locators_multimedia_product as lmp
from pages.utils import extract_numbers as en


class CustomerMultimediaProductPage(BasePage):

    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def check_header_page_product(self, name):
        time.sleep(3)
        title_header = self.find(lmp.header_name)
        assert title_header.text == name

    def check_add_to_cart(self, num):
        wait = WebDriverWait(self.driver, 10)
        try:
            click_add_to_cart = wait.until(EC.element_to_be_clickable(lmp.add_to_cart_loc))
            click_add_to_cart.click()
            print('Кнопка add to cart нажата')
        except Exception:
            print(f'Кнопка не была нажата! {Exception}')
        success_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(lmp.alert_loc)
        )

        assert en.extract_numbers_text(success_msg)[0] == num

    def check_button_basket(self, text):
        button_basket = self.find(lmp.button_basket_loc)
        button_basket.click()
        wait = WebDriverWait(self.driver, 10)
        text_page_cart = wait.until(EC.presence_of_element_located(lmp.text_cart_page_loc))
        assert text_page_cart.text == text

