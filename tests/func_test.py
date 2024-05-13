from page_object.MainPage import MainPage
from page_object.BasePage import BasePage
from page_object.AdminPage import AdminPage


class TestPart3:

    def test_LoginForAdmin(self, browser):
        browser.get("http://192.168.1.147:8081/administration/")
        AdminPage(browser).login_for_admin(login="user", password="12345678")
        BasePage(browser).wait_load_title(timeout=1, title_name="Dashboard")

    def test_SelectRandomProduct(self, browser):
        MainPage(browser).add_to_list_product()
        MainPage(browser).wait_alert_success()

    def test_ValueForMain(self, browser):
        value_first_element = BasePage(browser).get_value_first_price()
        BasePage(browser).set_currency_for_euro()
        new_value_first_element = BasePage(browser).get_value_first_price()
        assert value_first_element != new_value_first_element

    def test_ValueForCatalog(self, browser):
        browser.get("http://192.168.1.147:8081/en-gb/catalog/desktops")
        value_first_element = BasePage(browser).get_value_first_price()
        BasePage(browser).set_currency_for_euro(value="€ Euro")
        new_value_first_element = BasePage(browser).get_value_first_price()
        assert value_first_element != new_value_first_element
