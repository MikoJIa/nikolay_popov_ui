from selenium.webdriver.common.by import By

header_name = (By.TAG_NAME, 'h1')
add_to_cart_loc = (By.XPATH, '//a[@id="add_to_cart"]')
basket_icon_loc = (By.XPATH, '//ul[@class="navbar-nav align-items-center gap-2 flex-shrink-0 justify-content-end ps-3"]'
                             '//li[@class="o_wsale_my_cart  "] //sup[@data-order-id="6885"]')
alert_loc = (By.CSS_SELECTOR, "[role='alert']")
button_basket_loc = (By.XPATH,
                     '//a[@class="o_navlink_background btn position-relative rounded-circle p-1 text-center text-reset"]')
text_cart_page_loc = (By.XPATH, '//div[@class="js_cart_lines alert alert-info"]')