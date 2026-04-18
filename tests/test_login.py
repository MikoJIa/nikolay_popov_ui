import time


def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('test_name@gmail.com','123qwerty')
    time.sleep(2)
    login_page.check_alert_is('Wrong login/password')
