from selenium import webdriver
import pytest
from pages.customer_login import CustomerLogin
from pages.customer_cart import CustomerCartPage
from pages.customer_desks import CustomerDesks
from pages.customer_multimedia_product import CustomerMultimediaProductPage


@pytest.fixture
def driver(request):
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(20)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture
def login_page(driver):
    return CustomerLogin(driver)

@pytest.fixture
def cart_page(driver):
    return CustomerCartPage(driver)

@pytest.fixture
def desks_page(driver):
    return CustomerDesks(driver)

@pytest.fixture
def mult_product_page(driver):
    return CustomerMultimediaProductPage(driver)
