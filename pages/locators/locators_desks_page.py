from selenium.webdriver.common.by import By

all_desks_loc = (By.XPATH, '//tbody //td[@data-name="Product"]')
search_loc = (By.XPATH, '//div[@class="products_header btn-toolbar flex-nowrap align-items-center'
                        ' justify-content-between gap-3 mb-3"] //input[@class="search-query form-control'
                        ' oe_search_box border-0 bg-light border-0 text-bg-light"]')
button_loc = (By.XPATH, '//div[@class="products_header btn-toolbar flex-nowrap align-items-center justify-content-between gap-3 mb-3"]'
                        '//button[@class="btn oe_search_button btn btn-light"]')
result = (By.XPATH, '//tbody//td')
sort_by_loc = (By.XPATH, '//div[@class="o_sortby_dropdown dropdown dropdown_sorty_by d-none me-auto d-lg-inline-block"] //a[@class="dropdown-toggle btn btn-light"]')
product_price_loc = (By.XPATH, '//div[@class="product_price"] //span[@class="oe_currency_value"]')
select_low_to_high_loc = (By.XPATH, '//a[@role="menuitem"] //span[text()="Price - Low to High"]')


