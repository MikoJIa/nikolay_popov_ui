def test_correct_page_title(cart_page):
    cart_page.open_page()
    cart_page.check_page_title_is('Order overview')

def test_correct_text_info(cart_page):
    cart_page.open_page()
    cart_page.check_page_info_is('Your cart is empty!')

def test_page_cart_button_sign_in(cart_page):
    cart_page.open_page()
    cart_page.check_page_button_sing_in('Email', 'Password')

def test_page_cart_contact_us(cart_page):
    cart_page.open_page()
    cart_page.check_page_cart_contact_us('Contact Us')