from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators.locators_login import login_loc, pass_loc


class CustomerLogin(BasePage):
    page_url = '/web/login'

    def fill_login_form(self, email, password):
        email_field = self.find(login_loc)
        email_field.send_keys(email)

        password_field = self.find(pass_loc)
        password_field.send_keys(password)

        wait = WebDriverWait(self.driver, 5)
        element_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Log in"]')))
        element_button.click()

    def check_alert_is(self, text):
        wait = WebDriverWait(self.driver, 20)
        wrong = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@class="alert alert-danger"]')))
        assert wrong.text == text, 'Too many login failures, please wait a bit before trying again.'
