
def test_header_multimedia_product(mult_product_page):
    mult_product_page.open_page()
    mult_product_page.check_header_page_product('Office Design Software')

def test_add_to_cart(mult_product_page):
    mult_product_page.open_page()
    mult_product_page.check_add_to_cart('1')

def test_button_basket(mult_product_page):
    mult_product_page.open_page()
    mult_product_page.check_button_basket('Your cart is empty!')

