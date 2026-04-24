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

    def check_search_field(self):
        wait = WebDriverWait(self.driver, 20)
        search = wait.until(EC.presence_of_element_located(ldp.search_loc))
        search.send_keys('desk')
        button_submit = self.find(ldp.button_loc)
        button_submit.click()
        result_search = wait.until(EC.visibility_of_all_elements_located(ldp.result))
        return len(result_search)

    def check_the_table_count_search(self, num_tables):
        assert self.check_search_field() == num_tables

    def apply_sorting_by_desk_and_verify(self):
        wait = WebDriverWait(self.driver, 10)
        save_page = wait.until(EC.visibility_of_all_elements_located(ldp.product_price_loc))
        lst_usd = []  # список цен для каждого стола, до того как список строк переведён в список целых чисел.
        for desk in save_page:
            lst_usd.append(desk.text)
        sorted_by = wait.until(EC.element_to_be_clickable(ldp.sort_by_loc))
        sorted_by.click()
        select = self.find(ldp.select_low_to_high_loc)
        select.click()
        after_sorted_by = wait.until(EC.visibility_of_all_elements_located(ldp.product_price_loc))
        after_lst_usd = []  # отсортированный список цен на странице
        for desk in after_sorted_by:
            after_lst_usd.append(desk.text)

        assert self.func_sorted(lst_usd) == self.func_sorted(after_lst_usd)  # сравниваем два отсотировыанных
        # списка после выбора на странице sort by от меньшей цены к большей

