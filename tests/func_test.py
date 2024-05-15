import time

from page_object.main_page import MainPage
from page_object.base_page import BasePage
from page_object.admin_page import AdminPage
from page_object.registation_page import RegistrPage


class TestPart3:

    def test_login_for_admin(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        AdminPage(browser).login_for_admin(login="user", password="12345678")
        BasePage(browser).wait_load_title(timeout=1, title_name="Dashboard")

    def test_select_random_product(self, browser):
        MainPage(browser).add_to_list_product()
        MainPage(browser).wait_alert_success()

    def test_value_for_main(self, browser):
        value_first_element = BasePage(browser).get_value_first_price()
        BasePage(browser).set_currency_for_euro()
        new_value_first_element = BasePage(browser).get_value_first_price()
        assert value_first_element != new_value_first_element

    def test_value_for_catalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        value_first_element = BasePage(browser).get_value_first_price()
        BasePage(browser).set_currency_for_euro(value="€ Euro")
        new_value_first_element = BasePage(browser).get_value_first_price()
        assert value_first_element != new_value_first_element


class TestHW_PageObject:

    def test_add_product_for_admin(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        AdminPage(browser).login_for_admin(login="user", password="12345678")
        BasePage(browser).set_new_window("Dashboard")
        AdminPage(browser).open_catalog_product()
        BasePage(browser).set_new_window("Products")
        AdminPage(browser).add_product()

    def test_dell_product_for_admin(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        AdminPage(browser).login_for_admin(login="user", password="12345678")
        BasePage(browser).set_new_window("Dashboard")
        AdminPage(browser).open_catalog_product()
        BasePage(browser).set_new_window("Products")
        AdminPage(browser).del_element()
        BasePage(browser).switch_and_accept_alert()

    def test_registration_client(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb?route=account/register")
        RegistrPage(browser).set_data_user()
        BasePage(browser).set_new_window("Your Account Has Been Created!")
        RegistrPage(browser).continue_after_registr()
        time.sleep(3)
