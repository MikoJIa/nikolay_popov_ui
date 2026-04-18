from selenium.webdriver.common.by import By


title_loc = (By.XPATH, '//h3[@class="mb-4"]')
text_info_loc = (By.XPATH, '//div[@class="js_cart_lines alert alert-info"]')
button_sign_in = (By.XPATH, '//a[@class="btn btn-outline-secondary" and contains(text(), "Sign in")]')
text_email = (By.XPATH, '//label[@class="form-label" and contains(text(), "Email")]')
text_pass = (By.XPATH, '//label[text()="Password"]')
contact_us_loc = (By.XPATH, '//a[text()="Contact Us" and contains(@class, "oe_unremovable btn btn-primary btn_cta")][1]')
contact_title_loc = (By.TAG_NAME, 'h1')