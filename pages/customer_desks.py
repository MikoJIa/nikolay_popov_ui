import time
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.locators import locators_desks_page as ldp
from selenium.webdriver.support import expected_conditions as EC

class CustomerDesks(BasePage):
    page_url = '/shop/category/desks-1'

    def func_sorted(self, lst: list):
        new_lst = [i.replace(',', '') for i in lst]
        lst = [int(float(i)) for i in new_lst]
        return sorted(lst)


    def all_desks_on_page(self):
        wait = WebDriverWait(self.driver, 10)
        all_desks = wait.until(EC.visibility_of_all_elements_located(ldp.all_desks_loc))
        assert len(all_desks) == 9
        time.sleep(5)

    def search_field(self, number_product_page):
        wait = WebDriverWait(self.driver, 10)
        search = wait.until(EC.presence_of_element_located(ldp.search_loc))
        search.send_keys('desk')
        time.sleep(1)
        button_submit = self.find(ldp.button_loc)
        button_submit.click()
        time.sleep(1)
        result_search = wait.until(EC.visibility_of_all_elements_located(ldp.result))
        time.sleep(5)
        assert len(result_search) == number_product_page

    def sort_by_desk(self):
        wait = WebDriverWait(self.driver, 10)
        save_page = wait.until(EC.visibility_of_all_elements_located(ldp.product_price_loc))
        lst_usd = []  # список цен для каждого стола, до того как список строк переведён в список целых чисел.
        for desk in save_page:
            lst_usd.append(desk.text)
        sorted_by = wait.until(EC.visibility_of_element_located(ldp.sort_by_loc))
        time.sleep(1)
        sorted_by.click()
        time.sleep(1)
        select = self.find(ldp.select_low_to_high_loc)
        select.click()
        after_sorted_by = wait.until(EC.visibility_of_all_elements_located(ldp.product_price_loc))
        after_lst_usd = []  # отсортированный список цен на странице
        for desk in after_sorted_by:
            after_lst_usd.append(desk.text)
        time.sleep(5)
        assert self.func_sorted(lst_usd) == self.func_sorted(after_lst_usd)  # сравниваем два отсотировыанных
        # списка после выбора на странице sort by от меньшей цены к большей

